# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def isBalanced(self, root: TreeNode) -> bool:
#         if not root:
#             return True
#         return abs(self.height(root.right) - self.height(root.left)) <= 1 and self.isBalanced(
#             root.left) and self.isBalanced(root.right)
#
#     def height(self, root):
#         if not root:
#             return 0
#         return max(self.height(root.left), self.height(root.right)) + 1

# 自底向上的递归
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.height(root) >= 0

    def height(self, root):
        if not root:
            return 0
        lh = self.height(root.left)
        lr = self.height(root.right)
        if lh == -1 or lr == -1 or abs(lh - lr) > 1:
            return -1
        else:
            return max(self.height(root.left), self.height(root.right)) + 1


if __name__ == '__main__':
    s = Solution()
    # print(s.isBalanced([3, 9, 20, None, None, 15, 7]))
