class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10**9 + 7
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 0:
            return 0
        
        dp = [1,1,2]

        for i in range(3, n + 1):
            val = (dp[i - 3] + 2 * dp[i - 1]) % mod
            dp.append(val)

        return dp[-1]