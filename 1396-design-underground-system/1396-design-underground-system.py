class UndergroundSystem:

    def __init__(self):
        self.metrics = {} #(start,end) = [freq, totalTime]
        self.transactions = {} # id = [station, t]
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.transactions[id] = [stationName, t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        prevStation, prevTime = self.transactions[id]
        key = tuple([prevStation, stationName])
        time = t - prevTime
        if key not in self.metrics:
            self.metrics[key] = [1, time]
        else:
            self.metrics[key][0] += 1
            self.metrics[key][1] += time

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = tuple([startStation,endStation])
        return self.metrics[key][1] / self.metrics[key][0]        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)