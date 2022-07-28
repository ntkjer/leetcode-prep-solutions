class BrowserHistory:

    def __init__(self, homepage: str):
        self.pos = 0
        self.end = 0
        self.history = [homepage]

    def visit(self, url: str) -> None:
        self.pos += 1
        if len(self.history) == self.pos:
            self.history.append(url)
        else:
            self.history[self.pos] = url
        self.end = self.pos

    def back(self, steps: int) -> str:
        self.pos = max(self.pos - steps, 0)
        return self.history[self.pos]
    
    def forward(self, steps: int) -> str:
        self.pos = min(self.pos + steps, self.end)
        return self.history[self.pos]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)