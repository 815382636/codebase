from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归
    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     result = []
    #
    #     def pre(r):
    #         if r:
    #             result.append(r.val)
    #             pre(r.left)
    #             pre(r.right)
    #
    #     pre(root)
    #     return result

    # 迭代
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result, stack = [], [root]
        while stack:
            r = stack.pop()
            result.append(r.val)
            if r.right:
                stack.append(r.right)
            if r.left:
                stack.append(r.left)
        return result
