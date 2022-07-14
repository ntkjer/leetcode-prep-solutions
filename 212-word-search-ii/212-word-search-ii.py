class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        res = list()
        rows, cols = len(board), len(board[-1])
        
        trie = {}
        end = "$"
        visit = set()
        
        for word in words:
            root = trie
            for ch in word:
                if ch not in root:
                    root[ch] = {}
                root = root[ch]
            root[end] = True
        
        def backtrack(r, c, word, parent):
            if (r, c) in visit or not(0 <= r < rows) or not(0 <= c < cols):
                return False
            letter = board[r][c]
            if letter not in parent:
                return False
            
            visit.add((r, c))
            node = parent[letter]
            isMatch = node.pop(end, False)
            
            if isMatch:
                res.append(word + letter)
                
            backtrack(r + 1, c, word + letter, node)
            backtrack(r, c + 1, word + letter, node)
            backtrack(r - 1, c, word + letter, node)
            backtrack(r, c - 1, word + letter, node)
            
            visit.remove((r,c))
            
            if not node:
                parent.pop(letter)
                return
            
        
        for r in range(rows):
            for c in range(cols):
                root = trie
                backtrack(r, c, "", root)
                
        return res