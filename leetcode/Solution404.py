# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.result = 0

        def caculate(r, sign):
            if r.left is None and r.right is None and sign:
                self.result += r.val
                return
            if r.left:
                caculate(r.left, True)
            if r.right:
                caculate(r.right, False)

        if not root:
            return 0
        caculate(root, False)
        return self.result
