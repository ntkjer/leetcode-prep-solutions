class MinStack:

    def __init__(self):
        self.stack = [] # num, min

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append([val, val])
        else:
            prevMin = self.stack[-1][1]
            self.stack.append([val, min(val, prevMin)])
            
    def pop(self) -> None:
        res, prevMin = self.stack.pop()
        return res
            
        
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()