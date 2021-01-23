# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        self.head, self.next = None, None

        def caculate(r):
            if r.left:
                v, r.left = r.left, None
                caculate(v)
            if not self.head:
                self.head, self.next = r, r
            else:
                self.next.left, self.next.right, self.next = None, r, r

            if r.right:
                v, r.right = r.right, None
                caculate(v)

        caculate(root)
        return self.head
