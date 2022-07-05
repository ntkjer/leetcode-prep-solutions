class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = {}
        end = "#"
        res = list()
        rows, cols = len(board), len(board[0])
        visit = set()
        
        for word in words:
            root = trie
            for ch in word:
                if ch not in root:
                    root[ch] = {}
                root = root[ch]
            root[end] = True
        
        def dfs(r, c, parent, prefix):
            if (r, c) in visit or not(0 <= r < rows) or not (0 <= c < cols):
                return False
            
            letter = board[r][c]
            if letter not in parent:
                return False
            
            curr = parent[letter]
            isMatch = curr.pop(end, False)
            if isMatch:
                res.append(prefix + letter)
                            
            visit.add((r,c))
            dfs(r + 1, c, curr, prefix + letter)
            dfs(r, c + 1, curr, prefix + letter)
            dfs(r - 1, c, curr, prefix + letter)
            dfs(r, c - 1, curr, prefix + letter)

            visit.remove((r,c))
            if not curr:
                parent.pop(letter)
                
            
        
        for r in range(rows):
            for c in range(cols):
                root = trie
                dfs(r, c, root, "")
        
        return res