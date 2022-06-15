class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        small, large = self.small, self.large
        if len(small) == len(large):
            heappush(large, -heappushpop(small, -num))
        else:
            heappush(small, -heappushpop(large, num))

    def findMedian(self) -> float:
        small, large = self.small, self.large
        if len(small) == len(large):
            return (large[0] - small[0]) / 2
        else:
            return large[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()