class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans = 0
        north = south = east = west = 0
        for it in s:
            if it == 'N':
                north += 1
            if it == 'S':
                south += 1
            if it == 'E':
                east += 1
            if it == 'W':
                west += 1
            times1 = min(north, south, k)
            times2 = min(east, west, k - times1)
            ans = max(ans, self.count(north, south, times1) + self.count(east, west, times2))
        return ans
    def count(self, drt1, drt2, times):
        return abs(drt1 - drt2) + times * 2

        