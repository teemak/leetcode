class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        lo, hi = 1, x // 2

        while lo <= hi:
            mid = (hi + lo) // 2
            num = mid * mid

            if num > x:
                hi = mid - 1
            elif num < x:
                lo = mid + 1
            else:
                return mid

        return hi