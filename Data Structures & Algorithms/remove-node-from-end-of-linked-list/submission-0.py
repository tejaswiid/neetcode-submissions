# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0 
        dummy,first = head, head
        while head:
            head = head.next
            l += 1
        n = l - n 
        new = 0
        if n == 0: return dummy.next
        while first:
            if new == n - 1:
                first.next = first.next.next
            new += 1
            first = first.next
        return dummy
        
        