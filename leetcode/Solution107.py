from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack, result = [root], []
        while stack:
            mr = []
            for _ in stack[:]:
                v = stack.pop(0)
                mr.append(v.val)
                if v.left:
                    stack.append(v.left)
                if v.right:
                    stack.append(v.right)
            result.insert(0, mr)
        return result


if __name__ == '__main__':
    s = Solution()
    ro = TreeNode(3)
    ro.left = TreeNode(5)
    ro.right = TreeNode(6)
    print(s.levelOrderBottom(ro))
