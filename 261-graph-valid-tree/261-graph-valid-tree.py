class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj_list = {i: set() for i in range(n)}
        
        for edgeFrom, edgeTo in edges:
            adj_list[edgeFrom].add(edgeTo)
            adj_list[edgeTo].add(edgeFrom)
        
        visit = set()
        def dfs(node):
            if node in visit:
                return 
            visit.add(node)
            for nei in adj_list[node]:
                dfs(nei)
            return
        
        dfs(0)
            
        
        return len(visit) == n 