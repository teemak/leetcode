class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = list(map(int, s))
        n = len(digits) - 1
        l, r = digits[0], digits[1]
        multiplier = 1

        for i in range(1, n):
            multiplier = (multiplier * (n - i)) // i
            mod_mult = multiplier % 10

            l = (l + digits[i] * mod_mult) % 10
            r = (r + digits[i + 1] * mod_mult) % 10

        return l == r
