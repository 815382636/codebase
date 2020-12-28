from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            cu_queue = []
            for i in range(len(queue)):
                cu = queue.pop(0)
                cu_queue.append(cu.val)
                if cu.left:
                    queue.append(cu.left)
                if cu.right:
                    queue.append(cu.right)
            result.append(cu_queue)
        return result
