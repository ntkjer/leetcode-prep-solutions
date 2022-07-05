class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit = set()
        rows, cols = len(board), len(board[0])
        
        def solve(r, c, idx):
            if idx == len(word):
                return True
            if (r, c) in visit or not (0 <= r < rows) or not (0 <= c < cols):
                return False
            letter = board[r][c]
            if letter != word[idx]:
                return False
            visit.add((r,c))
            res = (solve(r + 1, c, idx + 1) or solve(r, c + 1, idx + 1) or
                  solve(r - 1, c, idx + 1) or solve(r, c - 1, idx + 1))
                   
            visit.remove((r,c))
            return res

        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if solve(r, c, 0):
                        return True
                    
        return False
                
        
                  