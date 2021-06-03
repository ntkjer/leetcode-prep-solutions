class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        score = 0 
        cur_score = 0 
        i = 0
        for j in range(len(nums)):
            while nums[j] in seen:
                cur_score -= nums[i]
                seen.remove(nums[i])
                i += 1

            cur_score += nums[j]
            seen.add(nums[j])
            score = max(cur_score, score) 
        return score