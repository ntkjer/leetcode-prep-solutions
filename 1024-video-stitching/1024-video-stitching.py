class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        furthest = 0
        prevEnd = float('-inf')
        count = 0
        
        clips.sort()
        for start, end in clips:
            if furthest >= time or start > furthest:
                break
            
            if prevEnd < start <= furthest:
                prevEnd = furthest
                count += 1            
            furthest = max(furthest, end)
        
        
        return count if furthest >= time else -1