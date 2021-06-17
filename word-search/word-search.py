class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N = len(board), len(board[-1])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        r = c = 0
        visited = set()

        def dfs(row, col, idx):
            if idx == len(word) - 1:
                return True

            for dx, dy in dirs:
                x, y = row + dx, col + dy
                if 0 <= x < M and 0 <= y < N and (x, y) not in visited:
                    if board[x][y] == word[idx + 1]:
                        visited.add((x, y))
                        if dfs(x, y, idx + 1):
                            return True
                        visited.remove((x, y))
            return False

        
        for r in range(M):
            for c in range(N):
                if board[r][c] == word[0]:
                    visited.add((r, c))
                    idx = 0
                    if dfs(r, c, idx):
                        return True
                    visited.remove((r, c))
        return False
                
