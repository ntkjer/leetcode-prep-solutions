class Solution:
    def knightDialer(self, n: int) -> int:
        max_int = (10 ** 9) + 7
        combinations = {0: [4, 6], 1: [6, 8], 2: [7, 9], 
                        3: [4, 8], 4: [0, 3, 9], 5: [], 
                        6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        
        moves = [1] * 10
        for i in range(n - 1):
            curr_moves = [0] * 10
            for i in range(10):
                for next_move in combinations[i]:
                    curr_moves[next_move] = (curr_moves[next_move] + moves[i]) % max_int
                    
            moves = curr_moves
        return sum(moves) % max_int