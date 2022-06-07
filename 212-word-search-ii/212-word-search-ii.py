class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[-1])
        
        trie = {}
        end = "$"
        visit = set()
        res = list()
        
        for word in words:
            node = trie
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node[end] = True
        
        
        def dfs(r, c, prefix, parent):
            if (r,c) in visit or not(0 <= r < ROWS) or not(0 <= c < COLS) or board[r][c] not in parent:
                return False

            
            visit.add((r,c))
            letter = board[r][c]
            
            node = parent[letter]
            match = node.pop(end, False)
            if match: 
                res.append(prefix + letter)
            dfs(r + 1, c, prefix + letter, node)
            dfs(r - 1, c, prefix + letter, node)
            dfs(r, c + 1, prefix + letter, node)
            dfs(r, c - 1, prefix + letter, node)
            if not node:
                parent.pop(letter)
            visit.remove((r,c))
            return True
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, "", trie)
        
        return res
                
        