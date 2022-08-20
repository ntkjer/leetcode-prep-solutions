class Solution:
    def dfs(self, origin):
        dest = self.flightMap[origin]
        while dest:
            nextDest = dest.pop()
            self.dfs(nextDest)
        self.result.append(origin)
        
    
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        from collections import defaultdict
        
        self.flightMap = defaultdict(list)
        
        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.flightMap[origin].append(dest)
            
        
        for origin, itinerary in self.flightMap.items(): 
            itinerary.sort(reverse = True)
            
        self.result = []
        self.dfs("JFK")
        return self.result[::-1]
    