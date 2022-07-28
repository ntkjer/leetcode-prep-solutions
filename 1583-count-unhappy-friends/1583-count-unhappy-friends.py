class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        for (u, v) in pairs:
            for pref in preferences[u]:
                if pref == v:
                    break
                graph[u].append(pref)
        
            for pref in preferences[v]:
                if pref == u:
                    break
                graph[v].append(pref)
        
        res = 0
        for node in list(graph.keys()):
            for cur_pref in graph[node]:
                if node in graph[cur_pref]:
                    res += 1
                    break # can onkly be unhappy once per person!
        return res