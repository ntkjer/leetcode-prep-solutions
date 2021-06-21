class Solution:
    def merge(self, first, second) -> List[int]:
        i, j = 0, 0
        result = list()
        while i < len(first) and j < len(second):
            if first[i] <= second[j]:
                result.append(first[i])
                i += 1
            else:
                result.append(second[j])
                j += 1

        result.extend(first[i:])        
        result.extend(second[j:])
        return result

    def sortArray(self, nums: List[int]) -> List[int]:
        N = len(nums) 
        if N <= 1:
            return nums

        first = self.sortArray(nums[N//2:])
        second = self.sortArray(nums[:N//2])
        
        result = self.merge(first, second)
        return result
    


        
        