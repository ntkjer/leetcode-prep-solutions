class LogSystem:

    def __init__(self):
        self.granularity_map = {"Year": 1, "Month": 2, "Day": 3, 
                                "Hour": 4, "Minute": 5, "Second": 6}
        self.logs = collections.defaultdict(int) # ts : uid

    def put(self, id: int, timestamp: str) -> None:
        self.logs[tuple(timestamp.split(":"))] = id

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        idx = self.granularity_map[granularity]
        res = list()
        
        start = tuple(start.split(":")[:idx])
        end = tuple(end.split(":")[:idx])
        
        
        for ts in self.logs.keys():
            if start <= ts[:idx] <= end:
                res.append(self.logs[ts])
                
        return res


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)