class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        
        clips.sort()
        
        prevEnd = float("-inf")
        count = 0
        end = 0
        for curStart, curEnd in clips:
            if end >= time or curStart > end:
                break
            
            if prevEnd < curStart <= end:
                prevEnd = end
                count += 1
            
            end = max(end, curEnd)
        
        return count if end >= time else -1