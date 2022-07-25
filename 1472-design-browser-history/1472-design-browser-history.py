class BrowserHistory:

    def __init__(self, homepage: str):
        self.ptr = 0
        self.history = [homepage]
        self.limit = 0
        
    def visit(self, url: str) -> None:
        self.ptr += 1
        if len(self.history) == self.ptr:
            self.history.append(url)
        else:
            self.history[self.ptr] = url
        self.limit = self.ptr  

    def back(self, steps: int) -> str:
        self.ptr = max(self.ptr - steps, 0)
        return self.history[self.ptr]
        
    def forward(self, steps: int) -> str:
        self.ptr = min(steps + self.ptr, self.limit)
        return self.history[self.ptr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)