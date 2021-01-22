from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        result = []

        def caculate(r):
            if r.children:
                for i in r.children:
                    caculate(i)
            result.append(r.val)

        caculate(root)
        return result
