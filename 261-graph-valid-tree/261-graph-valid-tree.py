class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n + 1)}
        if len(edges) != n - 1:
            return False
        
        for edgeFrom, edgeTo in edges:
            graph[edgeFrom].append(edgeTo)
            graph[edgeTo].append(edgeFrom)
        
        visit = set()
        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nei in graph[node]:
                dfs(nei)
                
        dfs(0)
        return len(visit) == n
        
        