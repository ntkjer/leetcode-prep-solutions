class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        res = list()
        
        def backtrack(node, partial):
            if node == len(graph) - 1:
                res.append(partial[:])
                return
            
            for nei in graph[node]:
                partial.append(nei)
                backtrack(nei, partial)
                partial.pop()
                
        backtrack(0, [0])
        return res