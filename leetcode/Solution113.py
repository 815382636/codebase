from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        result = []

        def path(r, s, arr):
            if not r:
                return
            if not r.left and not r.right and r.val == s:
                arr.append(r.val)
                result.append(arr)
                return
            path(r.left, s - r.val, arr + [r.val])
            path(r.right, s - r.val, arr + [r.val])

        path(root, sum, [])
        return result


if __name__ == '__main__':
    s = Solution()
    # print(s.pathSum())
