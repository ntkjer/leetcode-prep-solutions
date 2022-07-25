class UndergroundSystem:

    def __init__(self):
        self.customers = {} # id: (stationName, t)
        self.metrics = {}  # (start,end) : (elapsedTime, frequency)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = self.customers.get(id, []) + [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        prevStation, prevTime = self.customers[id]
        del (self.customers[id])
        
        key = tuple([prevStation, stationName])
        timeDelta = t - prevTime
        if key in self.metrics:
            self.metrics[key][0] += timeDelta
            self.metrics[key][1] += 1
        else:
            self.metrics[key] = [timeDelta, 1]
            
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = tuple([startStation, endStation])
        return self.metrics[key][0] / self.metrics[key][1]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)