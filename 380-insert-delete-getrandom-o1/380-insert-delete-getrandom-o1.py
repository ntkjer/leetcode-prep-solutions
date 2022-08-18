class RandomizedSet:

    def __init__(self):
        self.list = []
        self.items = {}

    def insert(self, val: int) -> bool:
        if val in self.items:
            return False
        idx = len(self.list)
        self.items[val] = idx
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.items:
            return False
        idx = self.items[val]
        lastElem = self.list[-1]
        
        self.items[lastElem] = idx
        self.list[idx], self.list[-1] = lastElem, val
        
        del self.items[val]
        self.list.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()