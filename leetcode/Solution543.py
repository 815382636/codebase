# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.result = 0

        def caculate(r):
            if r:
                if r.left or r.right:
                    le = caculate(r.left)
                    ri = caculate(r.right)
                    length = le + ri + 1
                    self.result = self.result if self.result >= length else length
                    return max(le, ri) + 1
                else:
                    self.result = self.result if self.result >= 1 else 1
                    return 1
            return 0

        caculate(root)
        return self.result - 1
