# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse(head,k):
            cur = dummy = head
            prev = None
            v = k
            while v and dummy:
                dummy = dummy.next
                v -= 1
            if not v:
                while k:
                    nxt = cur.next
                    cur.next = prev
                    prev = cur
                    cur = nxt 
                    k -= 1
                return prev,cur
            else:
                return None
        prev_tail,ans = None , None
        while head:
            arr = reverse(head,k)
            if not arr:
                break
        
            val,nxt = arr
            if not ans: ans = val
            if prev_tail:
                prev_tail.next = val
            prev_tail = head
            head = nxt
        if prev_tail: 
            prev_tail.next = head
        return ans if ans else head
               

            
        
        

        