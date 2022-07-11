class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def is_valid_block(block):
            block = [i for i in block if i != "."]
            return len(block) == len(set(block))
        
        def is_row_valid(board):
            for r in board:
                if not is_valid_block(r):
                    return False
            return True
        
        def is_col_valid(board):
            for c in zip(*board):
                if not is_valid_block(c):
                    return False
            return True
        
        def is_square_valid(board):
            for r in (0, 3, 6):
                for c in (0, 3, 6):
                    squares = [board[x][y] for x in range(r, r + 3) for y in range(c, c + 3)]
                    if not is_valid_block(squares):
                        return False
            return True
        
        def valid_sudoku(board):
            return is_row_valid(board) and is_col_valid(board) and is_square_valid(board)
        
        return valid_sudoku(board)