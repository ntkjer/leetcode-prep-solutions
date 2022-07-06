class RandomizedSet:

    def __init__(self):
        self.pos = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val not in self.pos:
            self.data.append(val)
            self.pos[val] = len(self.data) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        idx, last = self.pos[val], self.pos[self.data[-1]]
        self.data[idx] = self.data[last]
        self.pos[self.data[idx]] = idx
        
        self.data.pop()
        self.pos.pop(val,0)
        return True

    def getRandom(self) -> int:
        return self.data[random.randint(0, len(self.data) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()