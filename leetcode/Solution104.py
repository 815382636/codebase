# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        result = 0
        while queue:
            for i in range(len(queue)):
                cu = queue.pop(0)
                if cu.left:
                    queue.append(cu.left)
                if cu.right:
                    queue.append(cu.right)
            result += 1
        return result
