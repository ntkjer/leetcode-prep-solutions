class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # find a covered interval that reaches start to time
        clips.sort()
        prev_end, end, count = -1, 0, 0
        for cur_start, cur_end in clips:
            if cur_start > end or end >= time: 
                break
            if prev_end < cur_start <= end:
                prev_end = end
                count += 1
            end = max(end, cur_end)
        
        return count if end >= time else -1