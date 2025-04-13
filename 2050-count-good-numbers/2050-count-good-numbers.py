class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7

        def quick(x, y):
            ret, mul = 1, x
            while y > 0:
                if y % 2 == 1:
                    ret = ret * mul % mod
                mul = mul * mul % mod
                y //=2
            return ret
        return quick(5, (n + 1) // 2) * quick(4, n // 2) % mod