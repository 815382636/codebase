# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.result = 0x3f3f3f3f
        self.h = None

        def caculate(r):
            if r:
                caculate(r.left)
                if self.h is not None:
                    v = r.val - self.h
                    self.result = self.result if self.result <= v else v
                self.h = r.val
                caculate(r.right)

        caculate(root)
        return self.result
