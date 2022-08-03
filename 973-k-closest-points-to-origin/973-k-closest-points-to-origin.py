class Solution:
    def getDistance(self, point: List[int]):
        res = (point[0] ** point[0]) + (point[1] ** point[1])
        return res 
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for point in points:
            heapq.heappush(heap, (point[0] ** 2 + point[1] ** 2, point)) 
            
        #print(heap)
        res = list()
        
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
            
        return res