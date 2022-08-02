class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.aDiag = 0
        
    def move(self, row: int, col: int, player: int) -> int:
        n = self.n
        self.rows[row] += 1 if player == 1 else -1
        self.cols[col] += 1 if player == 1 else -1
        
        if row + col == (n - 1):
            self.aDiag += 1 if player == 1 else -1
        
        if row == col:
            self.diag += 1 if player == 1 else -1
        
        if abs(self.rows[row]) == n or abs(self.cols[col]) == n or abs(self.diag) == n or abs(self.aDiag) == n:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)