class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {}
        
        for num in arr:
            counts[num] = counts.get(num, 0) + 1
        
        
        freqSeen = set()
        for num, freq in counts.items():
            if freq in freqSeen:
                return False
            
            freqSeen.add(freq)
            
        return True