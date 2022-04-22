class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M, N = len(matrix), len(matrix[0])
        rowZero, colZero = False, False
        for r in range(M):
            for c in range(N):
                if matrix[r][c] == 0:
                    if r == 0:
                        rowZero = True
                    if c == 0:
                        colZero = True
                    
                    matrix[0][c] = matrix[r][0] = 0
                
        
        for r in range(1, M):
            for c in range(1, N):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if colZero:
            for r in range(M):
                matrix[r][0] = 0
        
        if rowZero:
            for c in range(N):
                matrix[0][c] = 0
        