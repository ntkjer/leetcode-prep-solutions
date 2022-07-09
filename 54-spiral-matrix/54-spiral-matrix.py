class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[-1])
        
        res = list()
        x, y = 0, -1
        direction = 1
        
        while (m * n) > 0:
            
            for _ in range(n):
                y += direction
                res.append(matrix[x][y])
                
                
            m -= 1
            
            for _ in range(m):
                x += direction
                res.append(matrix[x][y])
                
                
            n -= 1
            
            direction *= -1
            
        return res