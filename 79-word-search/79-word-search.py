class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[-1])
        
        visit = set()
        
        def dfs(r, c, pos):
            if pos == len(word):
                return True
            
            if ((r,c) in visit or 
                not (0 <= r < ROWS) or 
                not (0 <= c < COLS) or 
                board[r][c] != word[pos]):
                return False
            
            visit.add((r,c))
            res = (dfs(r + 1, c, pos + 1) or 
                   dfs(r, c + 1, pos + 1) or 
                   dfs(r - 1, c, pos + 1) or 
                   dfs(r, c - 1, pos + 1))
            visit.remove((r,c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                start_idx = 0
                if board[r][c] == word[start_idx]:
                    if dfs(r,c, start_idx):
                        return True
                    
                    
        return False