class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def is_valid_block(block):
            block = [i for i in block if i != '.']
            return len(block) == len(set(block))

        def are_rows_valid(board):
            for r in board:
                if not is_valid_block(r):
                    return False
            return True
        
        def are_cols_valid(board):
            for c in zip(*board):
                if not is_valid_block(c):
                    return False
            return True
        
        def are_squares_valid(board):
            for i in (0, 3, 6):
                for j in (0, 3, 6):
                    squares = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                    if not is_valid_block(squares): 
                        return False
            return True
        
        def valid_sudoku(board):
            return are_rows_valid(board) and are_cols_valid(board) and are_squares_valid(board)
            
        return valid_sudoku(board)
            
        