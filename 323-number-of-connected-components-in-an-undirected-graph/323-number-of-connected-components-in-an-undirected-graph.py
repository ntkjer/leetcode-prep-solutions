class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visit = set()
        adj_list = {i: set() for i in range(n)}
        for edgeA, edgeB in edges:
            adj_list[edgeA].add(edgeB)
            adj_list[edgeB].add(edgeA)
        
        
        def dfs(node):
            if node in visit: return
            
            visit.add(node)
            for nei in adj_list[node]:
                dfs(nei)
                
                
        res = 0
        
        for node in adj_list:
            if node not in visit:
                res += 1
                dfs(node)
        return res
            
        