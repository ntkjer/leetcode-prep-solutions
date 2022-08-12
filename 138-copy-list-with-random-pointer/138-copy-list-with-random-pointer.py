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
        if not head: return None
        res = {}
        
        dummy = ListNode(next=head)
        
        curr = head
        while curr:
        
            res[curr] = ListNode(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next is not None:
                res[curr].next = res[curr.next]
            else:
                res[curr].next = None
            
            if curr.random is not None:
                res[curr].random = res[curr.random]
            else:
                res[curr].random = None
            
            curr = curr.next
                
        return res[head]