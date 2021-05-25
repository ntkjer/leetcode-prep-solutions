class MedianFinder:

    def __init__(self):
        """
        We maintain the invariant that the two heaps will be balanced or at most differ by 1.
        This ensures that the top of both will hold the median element
        Either it is the average of both tops or large will hold one more element and return.
        """
        self.small = [] # max-heap, negate nums
        self.large = [] # min-heap
        
    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:    
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2
        else:
            return self.large[0]
        
            
                


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()