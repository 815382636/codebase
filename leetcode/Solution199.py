from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result, stack = [], [root]
        while stack:
            r = None
            for _ in stack[:]:
                r = stack.pop(0)
                if r.left:
                    stack.append(r.left)
                if r.right:
                    stack.append(r.right)
            result.append(r.val)
        return result
