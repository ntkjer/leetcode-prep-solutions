class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def valid_dir(x, y):
            if (x >= 0 and x < M) and (y >= 0 and y < N):
                return True
            return False
        
        directions = [(1, 0), (0, 1), (1, 1), (1, -1), (-1, 1), (0, -1), (-1, -1), (-1, 0)]
        M, N = len(board), len(board[-1])
        ALIVE = 2
        DEAD = -1
        
        for row in range(M):
            for col in range(N):
                total_neighbors = 0
                for dx, dy in directions:
                    i, j = row + dx, col + dy
                    if not valid_dir(i, j):
                        continue

                    if abs(board[i][j]) == 1:
                        total_neighbors += 1

                if board[row][col] == 1:
                    if total_neighbors < 2 or total_neighbors > 3:
                        # under/over populated
                        board[row][col] = DEAD
                    # rule 2 is implied
                elif board[row][col] == 0 and total_neighbors == 3:
                    board[row][col] = ALIVE
        
        for row in range(M):
            for col in range(N):
                if board[row][col] >= 1:
                    board[row][col] = 1
                else:
                    board[row][col] = 0
        
              
                    
                        
                        
                    
                        
                        
                
            