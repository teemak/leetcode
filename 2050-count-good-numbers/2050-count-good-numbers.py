class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7

        def expo(x, num):
            if num == 0:
                return 1
            elif num % 2 == 0:
                return expo(x ** 2 % mod, num // 2)
            return x * expo(x, num - 1) % mod

        return 5 ** (n % 2) * expo(20, n // 2) % mod