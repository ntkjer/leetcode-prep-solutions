"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        res = list()
        
        def solve(node):
            if not node: return
            res.append(Node(node.val))
            solve(node.child)
            solve(node.next)
            
            
        solve(head)
        prev_head = res[0]
        next_head = res[0]
        for i in range(1, len(res)):
            next_head = res[i]
            prev_head.next = next_head
            next_head.prev = prev_head
            prev_head = next_head
            
        return res[0]