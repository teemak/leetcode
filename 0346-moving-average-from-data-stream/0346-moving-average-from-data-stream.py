class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.max_size = size
        self.total = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.total += val

        if len(self.queue) > self.max_size:
            removed = self.queue.popleft()
            self.total -= removed
            
        return self.total / len(self.queue)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)