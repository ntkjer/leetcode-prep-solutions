class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        OLD_COLOR = grid[r0][c0]
        NEW_COLOR = color
        M, N = len(grid), len(grid[-1])
        visited = set()

        def dfs(r, c):
            if (r, c) in visited:
                return True
            if not (0 <= r < M and 0 <= c < N and grid[r][c] == OLD_COLOR):
                return False
            visited.add((r, c))

            if dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1) < 4:
                grid[r][c] = NEW_COLOR

            return True

        dfs(r0, c0)
        return grid
                    
            