class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0: 1}    
        csum = 0
        count = 0
        for num in nums:
            csum += num
            if csum - k in d:
                count += d[csum - k]

            if csum in d:
                d[csum] += 1
            else:
                d[csum] = 1
        
        return count
                
            