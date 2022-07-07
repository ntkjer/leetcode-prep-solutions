"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visit = {}
        
        def dfs(node):
            if not node: return
            if node in visit:
                return visit[node]
            
            curr = Node(node.val)
            visit[node] = curr
            for nei in node.neighbors:
                curr.neighbors.append(dfs(nei))
            
            return curr
        
        dfs(node)
        if len(visit) >= 1:
            return visit[node]
        else:
            return None