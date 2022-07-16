class UndergroundSystem:

    def __init__(self):
        self.checkins = {} # id: [station, time]
        self.journeys = {} # (startStation, endStation) : (total time, frequency)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkins.pop(id)
        
        journeyKey = (startStation, stationName)
        
        if journeyKey not in self.journeys:
            self.journeys[journeyKey] = [0, 0]
            
        self.journeys[journeyKey][0] += (t - startTime)
        self.journeys[journeyKey][1] += 1
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, totalTrips = self.journeys[(startStation, endStation)]
        return totalTime / totalTrips


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)