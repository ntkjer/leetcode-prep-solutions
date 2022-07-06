class HitCounter:

    def __init__(self):
        self.data = collections.deque()

    def hit(self, timestamp: int) -> None:
        self.data.append(timestamp)
        
    def getHits(self, timestamp: int) -> int:
        period = 60 * 5
        while self.data and timestamp - self.data[0] >= period:
            self.data.popleft()
        return len(self.data)

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)