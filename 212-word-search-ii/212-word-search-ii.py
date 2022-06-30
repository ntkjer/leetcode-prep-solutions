class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = list()
        rows, cols = len(board), len(board[-1])
        visit = set()
        
        trie = {}
        end = "$"
        
        for word in words:
            root = trie
            for ch in word:
                if ch not in root:
                    root[ch] = {}
                root = root[ch]
            root[end] = True
        
        def dfs(r, c, word, parent):
            if (r, c) in visit or not(0 <= r < rows) or not(0 <= c < cols):
                return 
            letter = board[r][c]
            if letter not in parent:
                return
            
            node = parent[letter]
            visit.add((r, c))
            match = node.pop(end, False)
            
            if match:
                res.append(word + letter)
                
                
            dfs(r + 1, c, word + letter, node)
            dfs(r, c + 1, word + letter, node)
            dfs(r, c - 1, word + letter, node)
            dfs(r - 1, c, word + letter, node)
            
            visit.remove((r,c))
            if not node:
                parent.pop(letter)
            
        
        for r in range(rows):
            for c in range(cols):
                root = trie
                dfs(r, c, "", root)
                
        return res