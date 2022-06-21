class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}

        for nodeA,nodeB in edges:
            graph[nodeA].append(nodeB)
            graph[nodeB].append(nodeA)
        
        visit = set()
        
        def dfs(node):
            if node in visit:
                return
            
            visit.add(node)
            for nei in graph[node]:
                dfs(nei)
            return
        
        connected = 0
        for node in graph:
            if node not in visit:
                connected += 1
                dfs(node)
                
                
        return connected