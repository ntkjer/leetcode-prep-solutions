class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit = set()
        ROWS, COLS = len(board), len(board[-1])
        
        def backtrack(r, c, idx):
            if idx == len(word):
                return True
            
            if (r,c) in visit or not(0 <= r < ROWS) or not(0 <= c < COLS) or board[r][c] != word[idx]:
                return False
            
            visit.add((r,c))    
            res = (backtrack(r + 1, c, idx + 1) or backtrack(r - 1, c, idx + 1) or 
                   backtrack(r, c + 1, idx + 1) or backtrack(r, c - 1, idx + 1))
            
            visit.remove((r,c))
            return res
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if word[0] == board[r][c]:
                    if backtrack(r, c, 0):
                        return True
        return False
            
        
        