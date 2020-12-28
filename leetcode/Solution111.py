# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        # result = 0
        # queue = [root]
        # while queue:
        #     result += 1
        #     for i in range(len(queue)):
        #         cu = queue.pop(0)
        #         if  not cu.left and not cu.right:
        #             return result
        #         if cu.left:
        #             queue.append(cu.left)
        #         if cu.right:
        #             queue.append(cu.right)
        # return -1
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.right), self.minDepth(root.left))
