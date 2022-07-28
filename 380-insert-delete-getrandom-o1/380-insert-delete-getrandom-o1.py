class RandomizedSet:

    def __init__(self):
        self.items = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.items:
            return False
        self.items[val] = len(self.list)
        self.list.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.items: 
            return False
        last_elem = self.list[-1]
        idx = self.items[val]
        
        self.items[last_elem] = idx
        self.list[idx] = last_elem
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