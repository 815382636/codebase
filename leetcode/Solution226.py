# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def change(r):
            if r:
                change(r.left)
                change(r.right)
                r.left, r.right = r.right, r.left

        change(root)
        return root


if __name__ == '__main__':
    s = Solution()
    # print(s.invertTree([4, 2, 7, 1, 3, 6, 9]))
