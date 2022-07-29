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
        
        elif bottomLeft.x == topRight.x and bottomLeft.y == topRight.y:
            return 1
            
        midX = (bottomLeft.x + topRight.x) // 2
        midY = (bottomLeft.y + topRight.y) // 2
        
        rect1 = self.countShips(sea, Point(midX, midY), bottomLeft) #bottom left
        rect2 = self.countShips(sea, Point(topRight.x, midY), Point(midX + 1, bottomLeft.y)) #bottom right
        rect3 = self.countShips(sea, Point(midX, topRight.y), Point(bottomLeft.x, midY + 1)) # upper left
        rect4 = self.countShips(sea, topRight, Point(midX + 1, midY + 1)) # upper right
        return rect1 + rect2 + rect3 + rect4

