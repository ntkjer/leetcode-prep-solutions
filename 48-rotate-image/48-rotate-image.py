class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        top = 0
        bottom = len(matrix) - 1
        
        while top < bottom:
            l = top
            r = bottom
            for i in range(r - l):
                
                topLeft = matrix[top][l + i]

                matrix[top][l + i] = matrix[bottom - i][l]
                
                matrix[bottom - i][l] = matrix[bottom][r - i]
                
                matrix[bottom][r - i] = matrix[top + i][r]
                
                matrix[top + i][r] = topLeft
        
            top += 1
            bottom -= 1
            