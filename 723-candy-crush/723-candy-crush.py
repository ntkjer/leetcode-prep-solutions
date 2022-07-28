class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(board), len(board[-1])
        
        while True:
            crushable = set()
            
            # mark vertically
            
            for r in range(rows - 2):
                for c in range(cols):
                    if board[r][c] and board[r][c] == board[r + 1][c] == board[r + 2][c]:
                        crushable.add((r, c))
                        crushable.add((r + 1, c))
                        crushable.add((r + 2, c))
                        
        
            # mark horizontally
            for r in range(rows):
                for c in range(cols - 2):
                    if board[r][c] and board[r][c] == board[r][c + 1] == board[r][c + 2]:
                        crushable.add((r, c))
                        crushable.add((r, c + 1))
                        crushable.add((r, c + 2))
                                    
            if not crushable:
                return board
            
            for r,c in crushable:
                board[r][c] = 0
            
            # let gravity fall
            for c in range(cols - 1, -1, -1):
                offset = 0
                for r in range(rows - 1, -1, -1):
                    k = r + offset
                    if (r,c) in crushable:
                        offset += 1
                    else:
                        board[k][c] = board[r][c]
                for r in range(offset):
                    board[r][c] = 0            
                
            