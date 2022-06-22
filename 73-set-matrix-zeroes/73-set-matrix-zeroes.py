class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowZero, colZero = False, False
        
        ROWS, COLS = len(matrix), len(matrix[-1])
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    if r == 0:
                        rowZero = True
                    if c == 0:
                        colZero = True
                    
                    matrix[0][c] = matrix[r][0] = 0
                    
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
 
        if colZero:
            for r in range(ROWS):
                matrix[r][0] = 0
                
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0