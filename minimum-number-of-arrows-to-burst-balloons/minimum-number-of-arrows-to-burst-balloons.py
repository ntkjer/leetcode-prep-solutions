class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda i: i[1])  
        
        last_endpoint = points[0][1]
        num_arrows = 1
        for p in points:
            if p[0] > last_endpoint:
                last_endpoint = p[1]
                num_arrows += 1
                
        return num_arrows
    
         