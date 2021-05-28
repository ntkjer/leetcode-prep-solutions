import collections
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        OLD_COLOR = image[sr][sc]
        M, N = len(image), len(image[-1])

        visited = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(x, y):
            if image[x][y] is not OLD_COLOR:
                return

            image[x][y] = newColor
            visited.add((x, y)) 

            for dx, dy in dirs:
                adj_x, adj_y = x + dx, y + dy
                if 0 <= adj_x < M and 0 <= adj_y < N and (adj_x, adj_y) not in visited:
                    dfs(adj_x, adj_y)

        dfs(sr, sc)
        return image
        
            