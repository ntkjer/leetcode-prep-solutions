class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows, cols = len(board), len(board[-1])
        # mark all cells that will live or die in next state
        directions = [(1, 0), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1), (-1, 0), (0, -1)]
        dead = -1
        alive = 2
        
        def is_valid_pos(x, y):
            if not (0 <= x < rows) or not (0 <= y < cols):
                return False
            return True
        
        for r in range(rows):
            for c in range(cols):
                curr_cell = board[r][c]
                neighbors = 0
                for dx, dy in directions:
                    x, y = dx + r, dy + c
                    if not is_valid_pos(x ,y):
                        continue
                    
                    if abs(board[x][y]) == 1:
                        neighbors += 1
                
                if board[r][c] == 1:
                    if neighbors < 2 or neighbors > 3:
                        board[r][c] = dead
                elif board[r][c] == 0 and neighbors == 3:
                    board[r][c] = alive
            
        for r in range(rows):
            for c in range(cols):
                if board[r][c] >= 1:
                    board[r][c] = 1
                else:
                    board[r][c] = 0