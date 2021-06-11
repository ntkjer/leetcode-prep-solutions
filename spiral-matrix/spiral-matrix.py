class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = list()
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        M, N = len(matrix), len(matrix[-1])
        visited = set()
        
        r = c = di = 0
        for _ in range(M * N):
            if (r, c) not in visited:
                visited.add((r, c))
                res.append(matrix[r][c])
                x, y = r + dirs[di][0], c + dirs[di][1]
                if 0 <= x < M and 0 <= y < N and (x, y) not in visited:
                    r, c = x, y
                else:
                    di = (di + 1) % len(dirs)
                    r, c = r + dirs[di][0], c + dirs[di][1]

        return res
        
        
        
 