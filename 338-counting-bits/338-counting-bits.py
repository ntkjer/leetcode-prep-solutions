class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def getOnes(n):
            res = 0
            while n:
                n &= (n - 1)
                res += 1
            return res 
        
        res = [0] * ((n) + 1)
        
        for i in range(1, n + 1):
            res[i] = 1 + res[i & (i - 1)]
            
        return res