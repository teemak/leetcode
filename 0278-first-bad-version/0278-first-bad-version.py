# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo, hi = 1, n

        while lo < hi:
            mid = (hi + lo) // 2
            if isBadVersion(mid): # check left
                hi = mid
            else:
                lo = mid + 1

        return lo
            