# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        preorderList = list()

        def preorderTraversal(root: TreeNode):
            if root:
                preorderList.append(root)
                preorderTraversal(root.left)
                preorderTraversal(root.right)

        preorderTraversal(root)
        size = len(preorderList)
        for i in range(1, size):
            prev, curr = preorderList[i - 1], preorderList[i]
            prev.left = None
            prev.right = curr

# 空间复杂度为O(1)
# class Solution:
#     def flatten(self, root: TreeNode) -> None:
#         curr = root
#         while curr:
#             if curr.left:
#                 predecessor = nxt = curr.left
#                 while predecessor.right:
#                     predecessor = predecessor.right
#                 predecessor.right = curr.right
#                 curr.left = None
#                 curr.right = nxt
#             curr = curr.right

