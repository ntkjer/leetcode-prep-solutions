"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        visited = {}
        
        def dfs(node):
            if node in visited:
                return visited[node]
            
            curr = Node(node.val)
            visited[node] = curr
            
            for neighbor in node.neighbors:
                curr.neighbors.append(dfs(neighbor))
            
            return curr
        
        if not node:
            return node
        res = dfs(node)
        return visited[node]