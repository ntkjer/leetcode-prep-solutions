"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        self.successor = None        
        
        def solve(node):
            if not node:
                return None
            
            if node.right:
                curr = node.right
                while curr.left:
                    curr = curr.left
                self.successor = curr
                return
            while node.parent and node == node.parent.right:
                node = node.parent
            self.successor = node.parent
            return 
                
        solve(node)
        return self.successor
