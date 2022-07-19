# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        # what is the slope, and can we binary search between topRight point to bottomLeft and collect answers?
            # find xRange and yRange? 
        if bottomLeft.x > topRight.x or bottomLeft.y > topRight.y:
            return 0
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        
        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return 1
        
        midX = (topRight.x + bottomLeft.x) // 2
        midY = (topRight.y + bottomLeft.y) // 2
        res = self.countShips(sea, Point(midX, midY), bottomLeft) + \
               self.countShips(sea, topRight, Point(midX + 1, midY + 1)) + \
               self.countShips(sea, Point(midX, topRight.y), Point(bottomLeft.x, midY + 1)) + \
               self.countShips(sea, Point(topRight.x, midY), Point(midX + 1, bottomLeft.y))
        return res