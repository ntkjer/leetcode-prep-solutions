class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows, cols = len(board), len(board[-1])
        save = set()
        capture = set()
        
        def dfs(r, c, visit):
            if (r,c) in visit:
                return
            if not (0 <= r < rows) or not(0 <= c < cols):
                return
            if board[r][c] != "O" or (r,c) in save:
                return
            
            visit.add((r,c))
            
            dfs(r + 1, c, visit)
            dfs(r, c + 1, visit)
            dfs(r - 1, c, visit)
            dfs(r, c - 1, visit)
            return
        
        
        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    dfs(r, c, save)
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) in save:
                    continue
                dfs(r, c, capture)
                
        for (x,y) in capture:
            board[x][y] = "X"