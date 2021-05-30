class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
#         c_min = nums[k]
#         left, right = [], []
#          
#         for i in range(k, -1, -1):
#             c_min = min(c_min, nums[i])
#             left.append(c_min)                
#         
#         c_min = nums[k]
#         for i in range(k, len(nums)):
#             c_min = min(c_min, nums[i])
#             right.append(c_min)
#         
#         
#         i, j = 0, len(nums) - 1
#         score = float('-inf') 
# 
#         while left and right:
#             score = max(score, min(right[-1], left[-1]) * (j - i + 1))
# 
#             if left[-1] < right[-1]:
#                 left.pop()
#                 i += 1
#             else:
#                 right.pop()
#                 j -= 1
# 

        score = 0
        c_min = nums[k]
        for i in range(k, -1, -1):
            c_min = min(c_min, nums[i])
            nums[i] = c_min
        
        
        c_min = nums[k]
        for i in range(k, len(nums)):
            c_min = min(c_min, nums[i])
            nums[i] = c_min

        i, j = 0, len(nums) - 1
        while i <= k <= j:
            score = max(score, min(nums[i], nums[j]) * (j - i + 1))    

            if nums[i] < nums[j]:
                i += 1
            else:
                j -= 1 

#        stack = [-1]
#        score = 0
#        for i, num in enumerate(nums + [0]):
#            while stack[-1] != -1 and num < nums[stack[-1]]:
#                top = stack.pop()
#                if not stack:
#                    break
#                height = nums[top]
#                width = i - stack[-1] - 1
#                if i > k and stack[-1] < k:
#                    score = max(score, height * width)    
#            stack.append(i)    
       #  while stack[-1] != -1:
       #      top = stack.pop()
       #      if not stack: break
       #      height = nums[top]
       #      width = len(nums) - stack[-1] - 1
       #      if stack[-1] < k:
       #          score = max(score, height * width)

        return score
            
            
        