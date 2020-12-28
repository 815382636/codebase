from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result, queue, sign = [], [root], True
        while queue:
            mr = []
            for _ in queue[:]:
                v = queue.pop(0)
                mr.append(v.val)
                if v.left:
                    queue.append(v.left)
                if v.right:
                    queue.append(v.right)
            if sign:
                result.append(mr)
            else:
                result.append(mr[::-1])
            sign = not sign
        return result


if __name__ == '__main__':
    s = Solution()
    # print(s.zigzagLevelOrder())
