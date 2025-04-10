class TwoSum:

    def __init__(self):
        self.diffs = defaultdict(int)

    def add(self, number: int) -> None:
        self.diffs[number] += 1

    def find(self, value: int) -> bool:
        return any(value - num in self.diffs and (value - num != num or self.diffs[num] > 1) for num in self.diffs)
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)