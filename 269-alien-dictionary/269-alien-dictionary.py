class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        
        graph = {c: set() for word in words for c in word}
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            
            minLength = min(len(w1), len(w2))
            
            if len(w1) > len(w2) and w1[:minLength] == w2[:minLength]:
                return ""
            
            for j in range(minLength):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break
                   
        visit = {}
        res = list()
        
        def dfs(node):
            if node in visit:
                return visit[node]
            
            visit[node] = True
            for nei in graph[node]:
                if dfs(nei): return True
                
            res.append(node)
            visit[node] = False
        
        for char in graph:
            if dfs(char): return ""
        
        res.reverse()
        return "".join(res)
        