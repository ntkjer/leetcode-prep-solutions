class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj_list = {i: set() for i in range(n + 1)}
        
        for first, second in edges:
            adj_list[first].add(second)
            adj_list[second].add(first)
        
        visit = set()
        
        def dfs(node):
            if node in visit:
                return 
            visit.add(node)
            for nei in adj_list[node]:
                dfs(nei)
        res = 0
        for i in range(n):
            if i not in visit:
                res += 1
                dfs(i)
        return res
        