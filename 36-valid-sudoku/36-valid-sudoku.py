class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def isValidBlock(block):
            block = [i for i in block if i != "."]
            return len(set(block)) == len(block)
        
        def isValidRow(board):
            block = []
            for r in board:
                if not isValidBlock(r): return False
            return True
        
        def isValidCol(board):
            for c in zip(*board):
                if not isValidBlock(c): return False
            return True
        
        def isValidSquare(board):
            for r in (0, 3, 6):
                for c in (0, 3, 6):
                    square = [board[x][y] for x in range(r, r + 3) for y in range(c, c + 3)]
                    if not isValidBlock(square):
                        return False
            return True
        
        return isValidCol(board) and isValidRow(board) and isValidSquare(board)