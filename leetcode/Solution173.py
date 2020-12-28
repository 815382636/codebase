# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.l = []
        self.index = 0

        def add(r):
            if r.left:
                add(r.left)
            self.l.append(r.val)
            if r.right:
                add(r.right)

        add(root)

    def next(self) -> int:
        v = self.l[self.index]
        self.index += 1
        return v

    def hasNext(self) -> bool:
        if self.index <= len(self.l) - 1:
            return True
        return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
