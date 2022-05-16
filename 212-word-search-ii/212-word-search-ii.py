class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        M, N = len(board), len(board[0])
        trie = {}
        end = "#"
        for w in words:
            node = trie
            for c in w:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node[end] = True
        
        visit, res = set(), list()
        
        def dfs(r, c, parent, word=""):
            if not(0 <= r < M) or not(0 <= c < N):
                return
            
            letter = board[r][c]
            if letter not in parent or (r,c) in visit:
                return
            
            visit.add((r,c))
            
            node = parent[letter]
            if end in node:
                res.append(word + letter)
                del node[end] # mark for deletion
                
            dfs(r + 1, c, node, word + letter)
            dfs(r - 1, c, node, word + letter)
            dfs(r, c + 1, node, word + letter)
            dfs(r, c - 1, node, word + letter)
            visit.remove((r,c))
            
            if not node:
                parent.pop(letter)
        
        for r in range(M):
            for c in range(N):
                dfs(r, c, trie)
        
        return res