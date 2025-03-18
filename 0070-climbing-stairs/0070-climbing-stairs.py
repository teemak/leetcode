class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt = 5**0.5
        phi = (1 + sqrt) / 2
        psi = (1 - sqrt) / 2

        return int((phi ** (n + 1) - psi ** (n + 1)) / sqrt)