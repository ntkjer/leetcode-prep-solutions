class BrowserHistory:

    def __init__(self, homepage: str):
        self.idx = 0
        self.history = [homepage]
        self.end = self.idx

    def visit(self, url: str) -> None:
        self.idx += 1
        if len(self.history) == self.idx:
            self.history.append(url)
        else:
            self.history[self.idx] = url
        self.end = self.idx

    def back(self, steps: int) -> str:
        self.idx = max(0, self.idx - steps)
        return self.history[self.idx]

    def forward(self, steps: int) -> str:
        self.idx = min(self.idx + steps, self.end)
        return self.history[self.idx]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)