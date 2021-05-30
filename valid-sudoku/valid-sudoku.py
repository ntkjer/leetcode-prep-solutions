class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        def is_valid_block(block):
            block = [i for i in block if i != '.']
            return len(block) == len(set(block))
        
        def is_valid_row(board):
            for row in board:
                if not is_valid_block(row):
                    return False
            return True
        
        def is_valid_col(board):
            for col in zip(*board):
                if not is_valid_block(col):
                    return False
            return True
        
        def is_valid_square(board):
            for i in (0, 3, 6):
                for j in (0, 3, 6):
                    square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                    if not is_valid_block(square):
                        return False
            return True
                    
        return (is_valid_row(board) and is_valid_col(board) and is_valid_square(board))