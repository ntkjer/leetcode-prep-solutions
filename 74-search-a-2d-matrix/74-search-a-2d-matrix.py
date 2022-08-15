class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[-1])
        
        top, bottom = 0, rows - 1
        
        while top <= bottom:
            mid = (bottom + top) // 2
            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                break
        
        if top > bottom:
            return False
        
        row = (top + bottom) // 2
        
        left, right = 0, cols - 1
        
        while left <= right:
            mid = (right + left) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False