class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(defaultdict)
        visited = set()
        
        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value
        
        
        def dfs(curr, target, partial):
            visited.add(curr)
            res = -1.0
            neighbors = graph[curr]
            if target in neighbors:
                res = partial * neighbors[target]
            else:
                for nei, val in neighbors.items():
                    if nei in visited:
                        continue
                    res = dfs(nei, target, val * partial)
                    if res != -1.0: 
                        break
            visited.remove(curr)
            return res
        
        res = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                val = -1.0
            elif dividend == divisor:
                val = 1.0
            else:
                val = dfs(dividend, divisor, 1)
            res.append(val)
        
        return res