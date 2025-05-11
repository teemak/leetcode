class Logger:

    def __init__(self):
        self.next_allowed = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.next_allowed or timestamp >= self.next_allowed[message]:
            self.next_allowed[message] = timestamp + 10
            return True
        return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)