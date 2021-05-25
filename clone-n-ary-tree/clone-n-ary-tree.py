"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':

#         def solve_recur(node):
#             if not node:
#                 return
#             curr = Node(node.val) 
#             for child in node.children:
#                 curr.children.append(solve_recur(child))
#             return curr
        if not root: 
            return None
        
        stack = [root]
        d = {} 
        d[root] = Node(root.val)

        while stack:
            node = stack.pop()
            for child in node.children:
                stack.append(child)
                d[child] = Node(child.val)
                d[node].children.append(d[child])

        return d[root]
        
            
                