# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getMid(l, r):
            slow = fast = l
            while fast != r and fast.next != r:
                fast = fast.next.next
                slow = slow.next
            return slow

        def create(left, right):
            if left == right:
                return None
            m = getMid(left, right)
            root = TreeNode(m.val)
            root.left = create(left, m)
            root.right = create(m.next, right)
            return root
        return create(head, None)


if __name__ == '__main__':
    s = Solution()
    # print(s.sortedListToBST([-10, -3, 0, 5, 9]))
