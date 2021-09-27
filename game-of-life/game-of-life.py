class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[-1])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)] 
        ALIVE = 2 
        DEAD = -1 

        def count_neighbors(i, j):
            count = 0
            return count
        
        def is_alive(i, j):
            return board[i][j] == 1
                
        for i in range(m):
            for j in range(n):
                live_neighbors = 0
                for dx, dy in dirs:
                    r = dx + i
                    c = dy + j
                    if (r < m and r >= 0) and (c < n and c >= 0) and abs(board[r][c]) == 1:
                        live_neighbors += 1

                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = DEAD
                
                if board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = ALIVE
        
        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
                    
                    
                    
        