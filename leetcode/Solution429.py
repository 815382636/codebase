from typing import List

"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        result, stack = [], [root]
        while stack:
            mr = []
            for _ in stack[:]:
                v = stack.pop(0)
                mr.append(v.val)
                if v.children:
                    for vc in v.children:
                        stack.append(vc)
            result.append(mr)
        return result


if __name__ == '__main__':
    s = Solution()
    # print(s.levelOrder())
