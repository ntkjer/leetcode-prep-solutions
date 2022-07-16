class UndergroundSystem:

    def __init__(self):
        self.checkinData = {} # id : (startTime, stationName)
        self.tripData = {} # (startStation , endStation) = (tripTime, frequency) 
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkinData[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startTime, startStation = self.checkinData.pop(id)
        # update the tripData
        route = (startStation, stationName)
        if route not in self.tripData:
            self.tripData[route] = [0, 0]
            
        self.tripData[route][0] += (t - startTime)
        self.tripData[route][1] += 1
        
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        totalTime, frequency = self.tripData[key]
        return totalTime / frequency


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)