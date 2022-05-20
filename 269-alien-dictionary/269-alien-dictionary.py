class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word }
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            length = min(len(w1), len(w2))
            
            if len(w1) > len(w2) and w1[:length] == w2[:length]:
                return ""
            
            for j in range(length):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visit = {}
        result = list()
        
        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True
            
            for nei in adj[c]:
                if dfs(nei):
                    return True
                
            visit[c] = False
            result.append(c)
        
        for c in adj:
            if dfs(c):
                return ""
        
        result.reverse()
        
        return "".join(result)