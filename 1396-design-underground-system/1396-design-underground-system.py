class UndergroundSystem:

    def __init__(self):
        self.metrics = defaultdict(list)
        self.trips = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.trips[id] = [stationName, t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        origin, prevTime = self.trips[id]
        key = tuple([origin, stationName])
        elapsedTime = t - prevTime
        
        if key not in self.metrics:
            self.metrics[key] = [elapsedTime, 1]
        else:
            self.metrics[key][0] += (t - prevTime)
            self.metrics[key][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        metrics = self.metrics[tuple([startStation, endStation])]
        total_time, freq = metrics
        return total_time / freq
    
# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)