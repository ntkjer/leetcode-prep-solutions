class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit = set()
        rows, cols = len(board), len(board[-1])
        
        
 
        def backtrack(r, c, idx):
            if idx == len(word):
                return True
            
            if (r, c) in visit:
                return False
            
            if not (0 <= r < rows) or not (0 <= c < cols):
                return False
            
            letter = board[r][c]
            if letter != word[idx]:
                return False
            visit.add((r, c))
           
            
            res = (backtrack(r + 1, c, idx + 1) or backtrack(r, c + 1, idx + 1) or
                   backtrack(r - 1, c, idx + 1) or backtrack(r, c - 1, idx + 1))
            visit.remove((r,c))
            return res 
        
        for r in range(rows):
            for c in range(cols):
                if word[0] == board[r][c]:
                    if backtrack(r, c, 0):
                        return True
        return False