# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        upper = 1
        lower = 0
        
        while reader.get(upper) < target:
            lower = upper
            upper <<= 2
       
        while lower <= upper:
            mid = lower + (upper - lower) // 2
            
            if reader.get(mid) == target:
                return mid

            elif reader.get(mid) > target:
                upper = mid - 1
            else:
                lower = mid + 1

        return -1
            
        