class Solution:
    def mySqrt(self, x: int) -> int:
        # need this for numbers smaller than 2 i.e. 1 is 1, 0 is 0
        if x < 2:
            return x

        # should start at 1 because of x = 2, half of 2 is 1 making it the hi
        # when x = 2 the result should be 1
        lo, hi = 1, x // 2

        # x = 8 [1,2,3,4]
        #        l   m h
        #        l m h

        # must iterate while lo is less than or equal to hi
        # i.e. 6 should return 2
        while lo <= hi:
            mid = (hi + lo) // 2
            if mid * mid > x:
                hi = mid - 1 # need this for 6 because it overshoots
            else:
                lo = mid + 1

        # need to return hi for overshoots i.e. 6
        return hi