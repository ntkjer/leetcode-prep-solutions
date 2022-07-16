class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # tree must have k - 1 edges 
        if len(edges) > n - 1:
            return False
        
        adj_list = {i: set() for i in range(n)}    
        for edgeA, edgeB in edges:
            adj_list[edgeA].add(edgeB)
            adj_list[edgeB].add(edgeA)
        
        visit = set()
        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nei in adj_list[node]:
                dfs(nei)
        
        dfs(0)
        return len(visit) == n
        