from typing import List

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        l = [root.val]
        st = []
        for i in range(len(root.children) - 1, -1, -1):
            st.append(root.children[i])
        while len(st) > 0:
            v = st.pop(-1)
            l.append(v.val)
            for j in range(len(v.children) - 1, -1, -1):
                st.append(v.children[j])
        return l


if __name__ == '__main__':
    s = Solution()
    # print(s.preorder([1, None, 3, 2, 4, None, 5, 6]))
