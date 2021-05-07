# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root:
            stack = [root]
            while stack:
                length = len(stack)
                for i in range(length):
                    nod = stack.pop(0)
                    if i != length - 1:
                        nod.next = stack[0]
                    if nod.left:
                        stack.append(nod.left)
                        stack.append(nod.right)
        return root


