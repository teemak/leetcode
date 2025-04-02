class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = list([0] * 101)
        self.current = -1
        self.length = 0
        self.visit(homepage)

    def visit(self, url: str) -> None:
        self.current += 1
        self.length = self.current + 1
        self.stack[self.current] = url

    def back(self, steps: int) -> str:
        self.current -= steps
        if self.current < 0:
            self.current = 0
        return self.stack[self.current]

    def forward(self, steps: int) -> str:
        self.current += steps
        if self.current > self.length - 1:
            self.current = self.length - 1
        return self.stack[self.current]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)