class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find the first consecutive decreasing pair of nums
        # find the first value larger than a[i]
        # swap a[i], a[k]
        # reverese all items from a[i + 1:len(a)]
        
        i = j = len(nums) - 1
        
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
           
        if i == 0:
            nums.reverse()
            return

        k = i - 1
        while j >= 0 and nums[j] <= nums[k]:
            j -= 1
        
        nums[k], nums[j] = nums[j], nums[k]
        
        r = len(nums) - 1
        while i < r:
            nums[i],nums[r] = nums[r], nums[i]
            i, r = i + 1, r - 1

        
        
         
    
            