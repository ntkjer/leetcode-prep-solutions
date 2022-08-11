class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {}
        for num in arr:
            counts[num] = counts.get(num, 0) + 1
        unique = set()
        
        for num, freq in counts.items():
            if freq in unique: 
                return False
            unique.add(freq)
        return True