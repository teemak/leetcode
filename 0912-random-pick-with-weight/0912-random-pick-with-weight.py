import random
import bisect

class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        curr_sum = 0
        for weight in w:
            curr_sum += weight
            self.prefix.append(curr_sum)
        self.total = curr_sum

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        return bisect.bisect_left(self.prefix, target)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()