class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # find subarray mins
        # add that subarray min_j for subarr_i
        
        max_int = (10 ** 9) + 7

        stack = [0] # idx, num
        arr = [0] + arr
        res = [0] * len(arr)
        for i, num in enumerate(arr):
            #print(stack)
            while stack and arr[stack[-1]] > num:
                stack.pop()
            
            j = stack[-1]
            res[i] = res[j] + num * (i - j)
            stack.append(i)
        
        return sum(res) % max_int