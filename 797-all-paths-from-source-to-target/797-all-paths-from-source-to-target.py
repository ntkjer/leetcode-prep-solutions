class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        res = list()
        def backtrack(node, path=[]):
            if node == len(graph) - 1:
                res.append(path[:])
                return
           
            for nei in graph[node]:
                path.append(nei)
                backtrack(nei, path)
                path.pop()
                
            return
        
        backtrack(0, [0])
        return res