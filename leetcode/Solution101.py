# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root or not root.left and not root.right:
            return True
        elif not (root.left and root.right):
            return False
        else:
            def judge(r1, r2):
                if not r1 and not r2:
                    return True
                elif not (r1 and r2):
                    return False
                else:
                    return r1.val == r2.val and judge(r1.left, r2.right) and judge(r1.right, r2.left)

            return judge(root.left, root.right)


if __name__ == '__main__':
    s = Solution()
    # print(s.isSymmetric([1, 2, 2, 3, 4, 4, 3]))
