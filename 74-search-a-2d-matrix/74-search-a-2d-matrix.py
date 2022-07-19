class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[-1])
        
        # binary search to find the correct row 
        top, bottom = 0, rows - 1
        while top <= bottom:
            curr_row = (top + bottom) // 2
            if target > matrix[curr_row][-1]:
                top = curr_row + 1
            elif target < matrix[curr_row][0]:
                bottom = curr_row - 1
            else:
                break
        if top > bottom: return False
        
        # binary search finding the value itself amongst the correct column
        row = (top + bottom) // 2
        
        l, r = 0, cols - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
            
        return False