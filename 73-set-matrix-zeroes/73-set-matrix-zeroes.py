class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowZero, colZero = False, False
        
        rows, cols = len(matrix), len(matrix[-1])
        
        for r in range(rows):
            for c in range(cols):
                if not matrix[r][c]:
                    if r == 0:
                        rowZero = True
                    if c == 0:
                        colZero = True
                    
                    matrix[r][0] = matrix[0][c] = 0
        
  
        for r in range(1, rows):
            for c in range(1, cols):
                if not matrix[0][c] or not matrix[r][0]:
                    matrix[r][c] = 0
       
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0
            
        if colZero:
            for r in range(rows):
                matrix[r][0] = 0