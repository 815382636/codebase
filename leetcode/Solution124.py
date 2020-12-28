# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.lar = -0x3f3f3f3f

        def mps(r):
            if not r:
                return 0
            nr = max(0, mps(r.right))
            nl = max(0, mps(r.left))
            self.lar = self.lar if self.lar >= nr + nl + r.val else nr + nl + r.val
            return r.val + max(nl, nr)

        mps(root)
        return self.lar


if __name__ == '__main__':
    s = Solution()
    # print(s.maxPathSum([1,2,3]))
