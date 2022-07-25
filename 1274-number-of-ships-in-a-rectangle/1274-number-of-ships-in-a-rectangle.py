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
        if bottomLeft.x > topRight.x or bottomLeft.y > topRight.y:
            return 0
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return 1
        
        midX = (topRight.x + bottomLeft.x ) // 2
        midY = (topRight.y + bottomLeft.y) // 2
        
        
        # bottomLeftRect = bottomLeft, Point(midX, midY)
        # bottomRightRect = Point(midX, bottomLeft.y), Point(bottomLeft.x, midY)
        # topLeftRect = Point(bottomLeft.x, midY + 1),Point(midX + 1, topRight.y)
        # topRightRect = Point(midX + 1, midY + 1), topRight
        rect1 = self.countShips(sea, Point(midX, midY), bottomLeft) # bottomLeft square
        rect2 = self.countShips(sea, Point(midX, topRight.y), Point(bottomLeft.x, midY + 1)) # topLeft square
        rect3 = self.countShips(sea, Point(topRight.x, midY), Point(midX + 1, bottomLeft.y)) # bottomRight squazre
        rect4 = self.countShips(sea, topRight, Point(midX + 1, midY + 1)) # topRight 
        return rect1 + rect2 + rect3 + rect4