class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        
        graph = collections.defaultdict(list)
        
        for u, v in pairs:
            for pref in preferences[u]:
                if pref == v: break
                graph[u].append(pref)
                
            for pref in preferences[v]:
                if pref == u: break
                graph[v].append(pref)
        
        unhappy = 0
        
        for node in list(graph.keys()):
            for pref in graph[node]:
                if node in graph[pref]:
                    unhappy += 1
                    break
        return unhappy