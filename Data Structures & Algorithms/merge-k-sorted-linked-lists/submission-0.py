# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        def traverse(lis):
            while lis:
                arr.append(lis.val)
                lis = lis.next
        for lis in lists:
            traverse(lis)
        arr.sort()
        dummy = head = ListNode()
        for a in arr:
            dummy.next = ListNode(a)
            dummy = dummy.next
        return head.next
        


        