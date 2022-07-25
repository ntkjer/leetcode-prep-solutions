class Solution:
    def knightDialer(self, n: int) -> int:
        
        neighbors = {0: (4, 6), 
                     1: (8, 6),
                     2: (7, 9),
                     3: (8, 4), 
                     4: (3, 9, 0), 
                     5: set(),
                     6: (1, 7, 0),
                     7: (2, 6),
                     8: (1, 3),
                     9: (2, 4)}  
        
        
        counts = [1] * 10
        
        max_int = (10 ** 9) + 7
        for i in range(n - 1):
            future_counts = [0] * 10
            for src in range(10):
                for dst in neighbors[src]:
                    future_counts[dst] = (future_counts[dst] + counts[src] ) % max_int
        
            counts = future_counts
            
        return sum(counts) % max_int