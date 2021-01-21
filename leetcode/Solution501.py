from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.result_c, self.result_f, self.rm_c, self.rm_f = 0, [], 0, 0

        def midfind(r):
            if r:
                midfind(r.left)
                if r.val == self.rm_f:
                    self.rm_c += 1
                else:
                    if self.result_c < self.rm_c:
                        self.result_f = [self.rm_f]
                        self.result_c = self.rm_c
                    elif self.result_c == self.rm_c:
                        self.result_f.append(self.rm_f)
                    self.rm_f, self.rm_c = r.val, 1

                midfind(r.right)

        midfind(root)
        if self.result_c < self.rm_c:
            return [self.rm_f]
        elif self.result_c == self.rm_c:
            self.result_f.append(self.rm_f)
            return self.result_f
        return self.result_f