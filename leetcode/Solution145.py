from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     result = []
    #
    #     def postord(r):
    #         if r:
    #             postord(r.left)
    #             postord(r.right)
    #             result.append(r.val)
    #
    #     postord(root)
    #     return result

    # 迭代
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result, stack = [], [root]
        while stack:
            r = stack.pop()
            result.append(r.val)
            if r.left:
                stack.append(r.left)
            if r.right:
                stack.append(r.right)
        result.reverse()
        return result
