# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.l = 0

        def level(r):
            if r:
                self.l += 1
                level(r.left)

        def f(num):
            m, r = bin(num), root
            for i in range(3, len(m)):
                if m[i] == '0':
                    r = r.left
                else:
                    r = r.right
            if r:
                return True
            return False

        level(root)
        left = pow(2, self.l - 1)
        right = pow(2, self.l)
        while left < right - 1:
            mid = left + (right - left) // 2
            if f(mid):
                left = mid
            else:
                right = mid
        return left
