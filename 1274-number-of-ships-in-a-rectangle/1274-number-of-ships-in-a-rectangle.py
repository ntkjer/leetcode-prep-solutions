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
        
        if topRight.x < bottomLeft.x or topRight.y < bottomLeft.y:
            return 0
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return 1
        
        midX = (topRight.x + bottomLeft.x) // 2
        midY = (topRight.y + bottomLeft.y) // 2
        
        rect1 = self.countShips(sea, Point(midX, midY), bottomLeft)
        rect2 = self.countShips(sea, Point(topRight.x, midY), Point(midX + 1, bottomLeft.y))
        rect3 = self.countShips(sea, topRight, Point(midX + 1, midY + 1))
        rect4 = self.countShips(sea, Point(midX, topRight.y), Point(bottomLeft.x, midY + 1))
        return rect1 + rect2 + rect3 + rect4