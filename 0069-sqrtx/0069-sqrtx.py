class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        lo, hi = 1, x

        while lo < hi:
            mid = (hi + lo) // 2
            if mid * mid > x:
                hi = mid
            else:
                lo = mid + 1

        return lo - 1