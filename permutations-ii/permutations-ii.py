class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []    
        def backtrack(comb, counts):
            if len(comb) == len(nums):    
                res.append(list(comb))
                return
            
            for num in counts:
                if counts[num] > 0:
                    comb.append(num)
                    counts[num] -= 1
                    backtrack(comb, counts)
                    comb.pop()
                    counts[num] += 1

        backtrack([], Counter(nums)) 
        return res