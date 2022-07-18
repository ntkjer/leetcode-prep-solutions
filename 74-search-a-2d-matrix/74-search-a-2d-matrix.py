class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first integer of reach row is gt than last integer of previous row
        rows, cols = len(matrix), len(matrix[-1])
        
        top, bottom = 0, rows - 1
        # isolate row
        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
        if top > bottom:
            return False
        
        row = (top + bottom) // 2
        l, r = 0, cols - 1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
            
        return False