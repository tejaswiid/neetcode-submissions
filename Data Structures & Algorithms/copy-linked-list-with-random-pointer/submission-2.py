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
        hmap = {None:None}
        dummy = cur = head
        while cur:
            copy = Node(cur.val)
            hmap[cur] = copy
            cur = cur.next
        while head:
            copy = hmap[head]
            copy.next = hmap[head.next]
            copy.random = hmap[head.random]
            head = head.next
        return hmap[dummy]
        