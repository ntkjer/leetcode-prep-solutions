"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        visit = {}
        
        def dfs(node):
            if node in visit:
                return visit[node]
            
            visit[node] = Node(node.val)
            
            for nei in node.neighbors:
                visit[node].neighbors.append(dfs(nei))
                
            return visit[node]
        
        dfs(node)
        return visit[node]