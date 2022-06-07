class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit = set()
        ROWS, COLS = len(board), len(board[-1])
        
        def dfs(r, c, idx=0):
            if idx == len(word):
                return True
            if (r,c) in visit or not 0 <= r < ROWS or not 0 <= c < COLS or word[idx] != board[r][c]:
                return False
  
            visit.add((r,c))
            res = (dfs(r + 1, c, idx + 1) or dfs(r, c + 1, idx + 1)
                   or dfs(r - 1, c, idx + 1) or dfs(r, c - 1, idx + 1))
            visit.remove((r,c))
            return res
            
        for r in range(ROWS):
            for c in range(COLS):
                start_idx = 0
                if board[r][c] == word[start_idx]:
                    if dfs(r, c, start_idx):
                        return True
        return False
        