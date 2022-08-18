class OrderedStream:

    def __init__(self, n: int):
        self.idx = 1
        self.stream = {}
        

    def insert(self, idKey: int, value: str) -> List[str]:
        res = list()
        self.stream[idKey] = value
        while self.idx in self.stream:
            res.append(self.stream[self.idx])
            self.idx += 1
            
        return res
        
# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)