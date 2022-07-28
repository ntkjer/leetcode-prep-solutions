class Solution:
    def knightDialer(self, n: int) -> int:
        
        
        moves = {0: [4, 6], 1: [6, 8], 2: [7, 9], 
                 3: [4, 8], 4: [0, 3, 9], 5: [], 
                 6: [0, 1, 7], 7: [6, 2], 8: [1, 3], 9: [4, 2]}
        
        
        total_moves = [1] * 10
        
        max_int = (10 ** 9) + 7
        
        for i in range(n - 1):
            curr_move = [0] * 10
            for src in range(10):
                for dst in moves[src]:
                    curr_move[dst] = (total_moves[src] + curr_move[dst]) % max_int                    
            total_moves = curr_move
        return sum(total_moves) % max_int