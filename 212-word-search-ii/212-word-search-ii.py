class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}    
        end = "$"
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]        
        result = list()
        visited = set()

        M, N = len(board), len(board[-1])

        for w in words:
            node = trie
            for ch in w:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node[end] = True
        
        
        def backtrack(r, c, parent, prefix):
            letter = board[r][c]
            if letter in parent:
                visited.add((r, c))    
                node = parent[letter]
                if end in node:
                    result.append(prefix + letter)
                    del node[end]
                    
                for dx, dy in dirs:
                    x, y = r + dx, c + dy
                    if 0 <= x < M and 0 <= y < N and (x, y) not in visited:
                        backtrack(x, y, node, prefix + letter)
                visited.remove((r, c))

                #optimize by removing matched leaf nodes from trie
                if not node:
                    parent.pop(letter)
        
        for r in range(M):
            for c in range(N):
                backtrack(r, c, trie, "")

        return result
            
                
            