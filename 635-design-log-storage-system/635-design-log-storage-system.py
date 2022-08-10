
class LogSystem:

    def __init__(self):
        self.data = {} # id: [timestamps]
        self.granularMap = {"Year": 1, "Month": 2, "Day": 3, "Hour": 4, "Minute": 5, "Second": 6}
        
        
    def put(self, id: int, timestamp: str) -> None:
        self.data[tuple(timestamp.split(":"))] = id
        
    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        idx = self.granularMap[granularity]
        
        start = tuple(start.split(":")[:idx])
        end = tuple(end.split(":")[:idx])
        
        res = list()
        for ts in self.data.keys():
            if start <= ts[:idx] <= end:
                res.append(self.data[ts])
                
        return res
        


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)