class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[-1])
        visit = set()
        
        trie = {}
        end = "$"
        
        for word in words:
            node = trie
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node[end] = True
        
        res = list()
        
        def dfs(r, c, parent, word):
            if (r,c) in visit or not(0 <= r < ROWS) or not(0 <= c < COLS):
                return False
            
            curr = board[r][c]
            if curr not in parent:
                return False
            
            node = parent[curr]
            
            visit.add((r,c))
            
            match = node.pop(end, False)
            if match:
                res.append(word+curr)
                
            dfs(r + 1, c, node, word+curr)
            dfs(r, c + 1, node, word+curr)
            dfs(r - 1, c, node, word+curr)
            dfs(r, c - 1, node, word+curr)
            
            visit.remove((r,c))
            if not node:
                parent.pop(curr)
                
        
        
        for r in range(ROWS):
            for c in range(COLS):
                root = trie
                dfs(r, c, root, "")
        
        return res