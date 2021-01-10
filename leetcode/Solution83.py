# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        n = head
        while n and n.next:
            if n.val == n.next.val:
                n.next = n.next.next
            else:
                n = n.next
        return head


if __name__ == '__main__':
    s = Solution()
    print(s.deleteDuplicates([1, 1, 2]))
