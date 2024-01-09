# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        first = dummy
        second = head
        cnt = 0
        while cnt < n:
            second = second.next
            cnt += 1
        while second:
            first = first.next
            second = second.next
        first.next = first.next.next

        return dummy.next
        

        

            
        