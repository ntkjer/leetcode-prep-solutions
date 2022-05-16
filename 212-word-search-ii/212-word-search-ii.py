class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = {}
        end = "$"
        M, N = len(board), len(board[0])
        result = set()
        visit = set()
        
        for word in words:
            curr = trie
            for ch in word:
                if ch not in curr:
                    curr[ch] = {}
                curr = curr[ch]
            curr[end] = True
    
        def dfs(r, c, parent, word):
            
            if (not(0 <= r < M) or not(0 <= c < N) or
               (r,c) in visit or board[r][c] not in parent):
                return
            
            visit.add((r,c))
            letter = board[r][c]
            node = parent[letter]
            
            if end in node:
                result.add(word + letter)
                del node[end]
                
            dfs(r + 1, c, node, word + letter)
            dfs(r - 1, c, node, word + letter)
            dfs(r, c + 1, node, word + letter)
            dfs(r, c - 1, node, word + letter)
            
            visit.remove((r,c))
            if not node:
                parent.pop(letter)
        
        for r in range(M):
            for c in range(N):
                dfs(r, c, trie, "")
                
        return list(result)