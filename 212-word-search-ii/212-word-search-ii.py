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

        M, N = len(board), len(board[0])
        result = list()
        
        
        def dfs(r, c, parent, prefix=""):

            
            if not(0 <= r < M) or not(0 <= c < N):
                return
            
            letter = board[r][c]
            if letter in parent:
                board[r][c] = "#"
                if letter not in parent:
                    return 
                node = parent[letter]
                match = node.pop(end, False)
                if match:
                    result.append(prefix + letter)

                for dx, dy in [(1, 0), (-1,0), (0, 1), (0, -1)]:
                    x, y = dx + r, dy + c
                    if (0 <= x < M and 0 <= y < N):
                        if board[x][y] in node:
                            dfs(x, y, node, prefix + letter)

                board[r][c] = letter
                if not node:
                    parent.pop(letter)
        
        for r in range(M):
            for c in range(N):
                dfs(r, c, trie)
                
        return result