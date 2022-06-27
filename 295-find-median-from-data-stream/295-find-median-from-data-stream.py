import heapq

class MedianFinder:

    def __init__(self):
        # small is maxheap, large is minheap
        # large will contain at most one more item
        self.small, self.large = [], []
    
    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self) -> float:
        if not len(self.small) == len(self.large):
            return self.large[0]
        else:
            return (self.large[0] - self.small[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()