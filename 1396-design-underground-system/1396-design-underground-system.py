class UndergroundSystem:

    def __init__(self):
        self.transactions = {} # id: station, time
        self.metrics = {} # (start,end) : (totalTime, freq)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.transactions[id] = self.transactions.get(id, []) + [stationName, t]
          
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        prevStation, prevTime = self.transactions[id]
        del self.transactions[id]
        
        key = tuple([prevStation, stationName])
        elapsedTime = t - prevTime
        if key in self.metrics:
            self.metrics[key][0] += elapsedTime
            self.metrics[key][1] += 1
        else:
            self.metrics[key] = [elapsedTime, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = tuple([startStation, endStation])
        return self.metrics[key][0] / self.metrics[key][1]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)