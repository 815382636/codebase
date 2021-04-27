# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
    #     self.sum = 0
    #
    #     def caculate(root):
    #         if root:
    #             if root.val < low:
    #                 caculate(root.right)
    #             else:
    #                 if root.val <= high:
    #                     self.sum += root.val
    #                     caculate(root.left)
    #                     caculate(root.right)
    #                 else:
    #                     caculate(root.left)
    #
    #     caculate(root)
    #     return self.sum

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)


if __name__ == '__main__':
    pass
