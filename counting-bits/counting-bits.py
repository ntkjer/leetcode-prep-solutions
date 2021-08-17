class Solution:
    def countBits(self, n: int) -> List[int]:
            
        def count_ones(x):
            """ 
            Naive approach Tn=O(nlgn)
            number of 1s is at most lg n of nlength int.
            at most we d
            """
            count = 0
            while x:
                x &= (x - 1)
                count += 1

            return count 
        
        res = [0] * (n + 1)
        
        for i in range(1, n + 1):
            #res[i] = count_ones(i)  
            res[i] = res[i & (i - 1)] + 1
            
        return res
    