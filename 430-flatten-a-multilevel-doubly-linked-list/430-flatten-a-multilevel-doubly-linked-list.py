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
        
        nodes = []
        
        def dfs(node):
            if not node:
                return
            
            nodes.append(Node(node.val))
            dfs(node.child)
            dfs(node.next)
            return
            
            
        
        dfs(head)
        new_head, prev_head = nodes[0], nodes[0]
        
        for i in range(1, len(nodes)):
            nodes[i].prev = prev_head
            prev_head.next = nodes[i]
            prev_head = prev_head.next

        return new_head