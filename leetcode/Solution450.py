# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left is None and root.right is None:
                root = None
            elif root.left and root.right:
                v = root.left
                if v.right is None:
                    root.val, root.left = v.val, v.left
                else:
                    while v.right.right is not None:
                        v = v.right
                    root.val, v.right = v.right.val, v.right.left
            elif root.left:
                root.val, root.left, root.right = root.left.val, root.left.left, root.left.right
            else:
                root.val, root.left, root.right = root.right.val, root.right.left, root.right.right
        return root
