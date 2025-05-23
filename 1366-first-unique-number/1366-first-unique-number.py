class FirstUnique:

    def __init__(self, nums: List[int]):
        self.queue = OrderedDict()
        self.unique = {}
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        if self.queue:
            return next(iter(self.queue))
        return -1

    def add(self, value: int) -> None:
        if value not in self.unique:
            self.unique[value] = True
            self.queue[value] = None
        elif self.unique[value]:
            self.unique[value] = False
            self.queue.pop(value, None)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)