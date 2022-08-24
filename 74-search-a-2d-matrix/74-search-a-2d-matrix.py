class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows, cols = len(matrix), len(matrix[-1])
        
        top = 0
        bottom = rows - 1
        
        # narrow down range for top and bottom
        
        while top <= bottom:
            m = (top + bottom) // 2
            if matrix[m][0] > target:
                bottom = m - 1
            elif matrix[m][-1] < target:
                top = m + 1
            else:
                break
        
        if top > bottom:
            return False
        
        row = (top + bottom) // 2
        
        left, right = 0, cols - 1
        while left <= right:
            m = (left + right) // 2
            if matrix[row][m] > target:
                right = m - 1
            elif matrix[row][m] < target:
                left = m + 1
            else:
                return True
        