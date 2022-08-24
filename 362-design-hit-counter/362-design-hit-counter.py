class HitCounter:

    def __init__(self):
        self.hits = collections.deque()
        self.period = 60 * 5
        
    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.hits and timestamp - self.hits[0] >= self.period:
            self.hits.popleft()
            
        return len(self.hits)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)