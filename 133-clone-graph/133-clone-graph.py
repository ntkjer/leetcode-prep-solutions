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
            for nei in node.neighbors:
                curr.neighbors.append(dfs(nei))
            
            return curr
        
        if not node:
            return node
        dfs(node)
        return visited[node]