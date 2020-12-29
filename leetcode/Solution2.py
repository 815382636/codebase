# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        k = result
        jinwei = 0
        while l1 or l2 or jinwei:
            mr = 0
            if l1:
                mr += l1.val
                l1 = l1.next
            if l2:
                mr += l2.val
                l2 = l2.next
            mr += jinwei
            result.next = ListNode(val=mr % 10)
            result = result.next
            jinwei = mr // 10
        return k.next


if __name__ == '__main__':
    s = Solution()
    # print(s.addTwoNumbers([2, 4, 3],
    #                       [5, 6, 4]))
