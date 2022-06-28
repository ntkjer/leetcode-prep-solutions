class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj_list = {i: set() for i in range(n + 1)}
        
        for nodeA, nodeB in edges:
            adj_list[nodeA].add(nodeB)
            adj_list[nodeB].add(nodeA)
            
        if len(edges) != n - 1:
            return False
        
        visit = set()
        def dfs(node):
            if node in visit:
                return 
            
            visit.add(node)
            for nei in adj_list[node]:
                dfs(nei)
            
            
        dfs(0)
            
        return len(visit) == n
        