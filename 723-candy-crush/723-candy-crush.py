class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        visit = set()
        
        # mark all crushable candies vertically
        # mark all crushable candies horizontally
        # crush all candies and mark as 0
        # shift candies from bottom to top
        
        rows, cols = len(board), len(board[-1])
        crushable = set()
        ready = False
        while not ready:
            ready = True
            crushable = set()

            for r in range(rows - 2):
                for c in range(cols):
                    if board[r][c] and board[r][c] == board[r + 1][c] == board[r + 2][c]:
                        crushable.add((r,c))
                        crushable.add((r + 1, c))
                        crushable.add((r + 2, c))
                        ready = False

            for r in range(rows):
                for c in range(cols - 2):
                    if board[r][c] and board[r][c] == board[r][c + 1] == board[r][c + 2]:
                        crushable.add((r,c))
                        crushable.add((r, c + 1))
                        crushable.add((r, c + 2))
                        ready = False
  
            if ready: return board
      
            for r,c in crushable:
                board[r][c] = 0
                
                
            for c in range(cols):
                offset = 0
                for r in range(rows - 1, -1, -1):
                    k = r + offset
                    if (r,c) in crushable:
                        offset += 1
                    else:
                        board[k][c] = board[r][c]
                for r in range(offset):
                    board[r][c] = 0
        
        
        return board