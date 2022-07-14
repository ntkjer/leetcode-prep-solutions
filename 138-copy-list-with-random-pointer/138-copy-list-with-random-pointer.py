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
        if not head:
            return head
        
        nodes = {}
        
        curr = head
        while curr:
            nodes[curr] = Node(x=curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next is not None:
                nodes[curr].next = nodes[curr.next]
            else:
                nodes[curr].next = None
                
            if curr.random is not None and curr.random in nodes:
                nodes[curr].random = nodes[curr.random]
            else:
                nodes[curr].random = None
            curr = curr.next
            
            
        return nodes[head]