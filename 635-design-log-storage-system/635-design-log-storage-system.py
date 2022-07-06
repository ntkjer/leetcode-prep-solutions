gmap = { 'Year': 1, 'Month': 2, 'Day': 3, 'Hour': 4, 'Minute': 5, 'Second': 6 }

class LogSystem:

    def __init__(self):
        self.data = {}

    def put(self, id: int, timestamp: str) -> None:
        t = tuple(timestamp.split(':'))
        self.data[t] = id

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        idx = gmap[granularity]
        s = tuple(start.split(':')[:idx])
        e = tuple(end.split(':')[:idx])
        
        res = list()
        for ts in self.data.keys():
            if s <= ts[:idx] <= e:
                res.append(self.data[ts])
                
        return res


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)