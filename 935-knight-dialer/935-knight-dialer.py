class Solution:
    def knightDialer(self, n: int) -> int:
        max_int = (10**9 + 7)
        moves = {0: (4, 6),
                1: (8, 6),
                2: (7, 9),
                3: (8, 4),
                4: (3, 9, 0), 
                5: set(),
                6: (1, 7, 0), 
                7: (2, 6),
                8: (1, 3),
                9: (2, 4)}
    
        current_counts = [1] * 10 # count each num from 0 -> 9
        for _ in range(n - 1):
            next_counts = [0] * 10
            for src_key in range(10):
                for dst in moves[src_key]:
                    next_counts[dst] = (next_counts[dst] + current_counts[src_key]) % (max_int)
                    
            current_counts = next_counts
            
        return sum(current_counts) % max_int