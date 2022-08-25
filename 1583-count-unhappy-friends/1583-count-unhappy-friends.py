class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        
        graph = collections.defaultdict(list)
        
        for u, v in pairs:
            for pref in preferences[u]:
                if v == pref:
                    break
                graph[u].append(pref)
                
            for pref in preferences[v]:
                if u == pref:
                    break
                graph[v].append(pref)
            
        
        res = 0
        for node in list(graph.keys()):
            for pref in graph[node]:
                if node in graph[pref]:
                    res += 1
                    break
        return res