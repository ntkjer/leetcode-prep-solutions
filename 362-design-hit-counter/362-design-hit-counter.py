class HitCounter:

    def __init__(self):
        self.data = {}

    def hit(self, timestamp: int) -> None:
        if timestamp not in self.data:
            self.data[timestamp] = 0    
        self.data[timestamp] += 1
        
    def getHits(self, timestamp: int) -> int:
        period = 60 * 5
        res = 0
        for ts in self.data.keys():
            if timestamp - period < ts <= timestamp:
                res += self.data[ts]
                
        return res

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)