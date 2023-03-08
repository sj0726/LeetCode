# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next

head = ListNode(1)
head.next = ListNode(2)
tail = head.next
tail.next = ListNode(3)
tail = tail.next
tail.next = ListNode(4)
tail = tail.next
print(Solution().swapPairs(head))