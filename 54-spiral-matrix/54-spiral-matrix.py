class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[-1])
        res = []
        
        x, y = 0, -1
        direction = 1
        
        while rows * cols > 0:
            for _ in range(cols):
                y += direction
                res.append(matrix[x][y])
                
            rows -= 1
            
            for _ in range(rows):
                x += direction
                res.append(matrix[x][y])
                
            cols -= 1
            direction *= -1
            
        
        return res