class RandomizedSet:

    def __init__(self):
        self.list = []
        self.items = {}

    def insert(self, val: int) -> bool:
        if val in self.items: return False
        idx = len(self.items)
        self.list.append(val)
        self.items[val] = idx
        return True

    def remove(self, val: int) -> bool:
        if val not in self.items: 
            return False
        removeIdx = self.items[val]
        lastElem = self.list[-1]
        self.list[removeIdx] = lastElem
        self.list.pop()
        self.items[lastElem] = removeIdx
        del self.items[val]
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()