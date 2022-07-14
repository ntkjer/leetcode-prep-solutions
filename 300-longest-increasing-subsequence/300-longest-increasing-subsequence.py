class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        sub = [nums[0]]
        for num in nums[1:]:
            idx = bisect_left(sub, num)
        
            if idx == len(sub):
                sub.append(num)
            else:
                sub[idx] = num
                
        return len(sub)
    
    