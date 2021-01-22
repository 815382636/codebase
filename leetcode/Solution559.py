# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        self.result = 0

        def caculate(r, h):
            if r.children:
                for i in r.children:
                    caculate(i, h + 1)
            else:
                self.result = self.result if self.result >= h else h

        caculate(root, 1)
        return self.result
