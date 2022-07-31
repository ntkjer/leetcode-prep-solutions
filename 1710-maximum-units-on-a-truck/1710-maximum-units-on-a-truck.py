class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        res = 0
        boxTypes.sort(key = lambda i: i[1], reverse=True)
        
        for size, unit in boxTypes:
            if truckSize > size:
                truckSize -= size
                res += size * unit
            else:
                res += truckSize * unit
                break
        return res
                