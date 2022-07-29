class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 1
        self.values = {}
        
    def insert(self, idKey: int, value: str) -> List[str]:
        self.values[idKey] = value
        res = list()
        while self.ptr in self.values:
            res.append(self.values[self.ptr])
            self.ptr += 1
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)