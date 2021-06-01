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
        if not node.left and not node.right and not node.parent:
            return self.successor
        
        def inorder(node):
            if not node:
                return 
            left = inorder(node.left)
            self.prev = node
            right = inorder(node.right)
            
        def solve(node):
            if not node:
                return None
            
            if node.right:
                curr = node.right
                while curr.left:
                    curr = curr.left
                self.successor = curr
                return

            else:
                curr = node
                parent = curr.parent
                while curr and parent and curr != parent.left:
                    curr = curr.parent
                    parent = parent.parent

                if parent:
                    self.successor = parent
                return
        solve(node)
        return self.successor
