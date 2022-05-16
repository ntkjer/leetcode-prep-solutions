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
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        
        def validPos(x,y):
            if not(0 <= x < M) or not(0 <= y < N):
                return False
            return True
        
        def dfs(r, c, parent, word=""):
            if not validPos(r,c):
                return  
            letter = board[r][c]
            if letter not in parent or (r,c) in visit:
                return
            
            visit.add((r,c))
            
            node = parent[letter]
            if end in node:
                res.append(word + letter)
                del node[end] # mark for deletion
            for dx, dy in directions:
                x, y = dx + r, dy + c
                if validPos(x,y) and (x,y) not in visit:
                    dfs(x, y, node, word + letter)
                    
            visit.remove((r,c))
            if not node:
                parent.pop(letter)
        
        
        for r in range(M):
            for c in range(N):
                dfs(r, c, trie)
        
        return res