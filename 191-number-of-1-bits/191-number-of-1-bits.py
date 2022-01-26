class Solution:
    def hammingWeight(self, n: int) -> int:
        num_ones = 0
        while n:
            num_ones += n & 1
            n >>= 1
            
        return num_ones
            
