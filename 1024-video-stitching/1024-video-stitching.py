class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        
        prev = -1
        furthest = 0
        count = 0
        
        clips.sort()
        for start, end in clips:
            if start > furthest or furthest >= time:
                break
            
            if prev < start <= furthest:
                prev = furthest 
                count += 1
            
            furthest = max(furthest, end)
             
        return count if furthest >= time else -1