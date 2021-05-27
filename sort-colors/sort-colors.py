class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Dutch national flag!! 
        
        We dividie the array into four sections:
        Entries from 0 up to (but not including) i are values less than mid,
        entries from i up to (but not including) j are values equal to mid,
        entries from j up to (and including) k are values not yet sorted, and
        entries from k + 1 to the end of the array are values greater than mid. 

        """
        N = len(nums)
        i = 0
        curr = 0
        k = N - 1

        while curr <= k:
            if nums[curr] == 0:
                nums[curr], nums[i] = nums[i], nums[curr]
                i += 1
                curr += 1

            elif nums[curr] == 2:
                nums[curr], nums[k] = nums[k], nums[curr]
                k -= 1
                
            else:
                curr += 1
            
            
            
        
        
        
                
                
        

        
            
                
            
            
            
        