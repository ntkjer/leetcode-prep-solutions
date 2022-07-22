class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        # there is a relationship between chars that are implicit
        # is there a topoligical ordering that we can extract from the words?
        
        # t > f?
        graph = {c: set() for word in words for c in word}
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break
        
        
        res = list()
        visit = {}
        
        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True
            for nei in graph[c]:
                if dfs(nei):
                    return True
            res.append(c)
            visit[c] = False
        
        for c in graph:
            if dfs(c): return ""
            
        res.reverse()
        return "".join(res)