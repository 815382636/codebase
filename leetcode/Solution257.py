from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        result = []

        def depth(r, s):
            if r:
                v = s + '->' + str(r.val)
                if not r.left and not r.right:
                    result.append(v[1:])
                    return
                if r.left:
                    depth(r.left, v)
                if r.right:
                    depth(r.right, v)

        depth(root, '')
        return result


if __name__ == '__main__':
    s = Solution()
    # print(s.binaryTreePaths())
