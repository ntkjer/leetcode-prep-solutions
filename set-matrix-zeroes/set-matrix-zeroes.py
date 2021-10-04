class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_col_has_zero, first_row_has_zero = False, False   
        m, n = len(matrix), len(matrix[-1])
        
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    if r == 0:
                        first_row_has_zero = True
                    if c == 0:
                        first_col_has_zero = True
                    matrix[r][0] = matrix[0][c] = 0
                   
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
                     
        if first_row_has_zero:
            for col in range(n):
                matrix[0][col] = 0

        if first_col_has_zero:
            for row in range(m):
                matrix[row][0] = 0
          
                
                
                    
                                
                        
                    