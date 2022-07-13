class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = list()
        n = len(nums) - 1
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n
            while j < k:
                cur = nums[i] + nums[j] + nums[k]
                if cur == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    
                    while j < n and nums[j] == nums[j + 1]:
                        j += 1
                        
                    while k > j and nums[k] == nums[k - 1]: 
                        k -= 1
                    
                    j, k = j + 1, k - 1
                    
                elif cur > 0:
                    k -= 1
                else:
                    j += 1
        return res