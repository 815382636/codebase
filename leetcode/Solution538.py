# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:

        self.midSum = 0

        def mid(r):
            if r.right:
                mid(r.right)

            r.val = r.val + self.midSum
            self.midSum = r.val

            if r.left:
                mid(r.left)

        if root:
            mid(root)
        return root
