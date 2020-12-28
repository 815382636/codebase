# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        root = None
        if inorder:
            root = TreeNode(postorder[-1])
            index = inorder.index(postorder[-1])
            root.left = self.buildTree(inorder[:index], postorder[:index])
            root.right = self.buildTree(inorder[index + 1:], postorder[index:-1])
        return root


if __name__ == '__main__':
    s = Solution()
    print(s.buildTree([9, 3, 15, 20, 7],
                      [9, 15, 7, 20, 3]))
