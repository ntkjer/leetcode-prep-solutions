class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        curr_cap = 0
        
        stubs = [] 
        
        for trip in trips:
            stubs.append((trip[1], trip[0])) # start
            stubs.append((trip[2], -trip[0])) # end
        
        stubs.sort()

        for location, cap in stubs:
            curr_cap += cap
            if curr_cap > capacity:
                return False

        return True
           