# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generate(start, end):
            if start > end:
                return [None, ]
            al = []
            for i in range(start, end + 1):
                le = generate(start, i - 1)
                ri = generate(i + 1, end)
                for j in le:
                    for k in ri:
                        t = TreeNode(i)
                        t.left = j
                        t.right = k
                        al.append(t)
            return al
        return generate(1, n) if n else []
