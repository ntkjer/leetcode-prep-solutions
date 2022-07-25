class OrderedStream:

    def __init__(self, n: int):
        self.data = {}
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.data[idKey] = value
        res = list()
        while self.ptr in self.data:
            res.append(self.data[self.ptr])
            self.ptr += 1
            
        return res

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)