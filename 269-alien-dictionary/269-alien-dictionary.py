class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        graph = {c: set() for word in words for c in word}
        
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            minLength = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:minLength] == word2[:minLength]:
                return ""
            for j in range(minLength):
                if word1[j] != word2[j]:
                    graph[word1[j]].add(word2[j])
                    break
                    
        res = list()
        visit = {}
        
        def dfs(char):
            if char in visit:
                return visit[char]
            
            visit[char] = True
            
            for nei in graph[char]:
                if dfs(nei): 
                    return True
                
            res.append(char)
            visit[char] = False
   
        
        for char in graph:
            if dfs(char): return ""
    
        res.reverse()        
        return "".join(res)
        