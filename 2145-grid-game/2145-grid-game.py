class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        top_sum = [0] * (n + 1)
        bot_sum = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            top_sum[i] = top_sum[i+1] + grid[0][i]
        for i in range(n):
            bot_sum[i+1] = bot_sum[i] + grid[1][i]

        result = float('inf')
        for i in range(n):
            top = top_sum[i+1]
            bot = bot_sum[i]
            result = min(result, max(top, bot))
        return result