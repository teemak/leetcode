class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k -= 1

        while k > 0:
            step = self.helper(n, curr, curr + 1)
            if step <= k:
                curr += 1
                k -= step
            else:
                curr *= 10
                k -= 1
        return curr

    def helper(self, n, p1, p2):
        steps = 0
        while p1 <= n:
            steps += min(n + 1, p2) - p1
            p1 *= 10
            p2 *= 10
        return steps
        