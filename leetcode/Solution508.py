from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        result = {}

        def sonSum(r):
            s = r.val
            if r.left:
                s += sonSum(r.left)
            if r.right:
                s += sonSum(r.right)
            if s not in result:
                result[s] = 1
            else:
                result[s] += 1
            return s
        if root:
            sonSum(root)
        m = max(result.values())
        rr = []
        for i in result.keys():
            if result[i] == m:
                rr.append(i)
        return rr

