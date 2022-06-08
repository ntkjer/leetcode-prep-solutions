class Solution:
    def reverseBits(self, n: int) -> int:
        power = 31
        res = 0
        while n:
            res += (n & 1) << power
            n >>= 1
            power -= 1
        return res