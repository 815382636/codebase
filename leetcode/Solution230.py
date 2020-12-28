# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k, self.result = k, 0

        def find(r):
            if r and self.k > 0:
                if r.left:
                    find(r.left)
                self.k -= 1
                if self.k == 0:
                    self.result = r.val
                    return
                if r.right:
                    find(r.right)

        find(root)
        return self.result


if __name__ == '__main__':
    s = Solution()
    # print(s.kthSmallest())
