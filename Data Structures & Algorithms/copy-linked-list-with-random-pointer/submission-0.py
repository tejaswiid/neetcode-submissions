"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        loopup = {None:None}
        cur = dummy = head
        while head:
            copy = Node(head.val)
            loopup[head] = copy
            head = head.next
        while cur:
            copy = loopup[cur]
            copy.next = loopup[cur.next]
            copy.random = loopup[cur.random]
            cur = cur.next
        return loopup[dummy]

            
        