from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        root = None
        if preorder:
            root = TreeNode(preorder[0])
            index = inorder.index(preorder[0])
            root.left = self.buildTree(preorder[1:index + 1], inorder[:index])
            root.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return root


if __name__ == '__main__':
    s = Solution()
    # print(s.buildTree([3, 9, 20, 15, 7],
    #                   [9, 3, 15, 20, 7]))
