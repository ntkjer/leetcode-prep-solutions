class Solution:
    def knightDialer(self, n: int) -> int:
        
        moves = {1: [6, 8], 2: [7, 9], 3: [8, 4], 
                 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 
                 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        
        max_int = (10 ** 9) + 7
        
        prev_state = [1] * 10
        for i in range(n - 1):
            curr_state = [0] * 10
            for start in range(10):
                for end in moves[start]:
                    curr_state[end] = (prev_state[start] + curr_state[end] ) % max_int
            prev_state = curr_state
        
        return sum(prev_state) % max_int
                