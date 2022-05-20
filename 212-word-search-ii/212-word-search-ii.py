class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = {}
        end = "$"
        
        for word in words:
            node = trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node[end] = True
        
        visit = set()
        ROWS, COLS = len(board), len(board[0])
        result = list()
        
        def dfs(r, c, parent, prefix=""):
            if ((r,c) in visit or not(0 <= r < ROWS) 
                or not(0 <= c < COLS) or board[r][c] not in parent):
                return False
            visit.add((r,c))
            letter = board[r][c]
            node = parent[letter]
            match = node.pop(end, False)
            if match:
                result.append(prefix + letter)
            
            dfs(r + 1, c, node, prefix + letter)
            dfs(r - 1, c, node, prefix + letter)
            dfs(r, c + 1, node, prefix + letter)
            dfs(r, c - 1, node, prefix + letter)
            
            visit.remove((r,c))
            
            if not node:
                parent.pop(letter)
                
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie, "")
        
        return result