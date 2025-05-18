class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # best = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         profit = prices[j] - prices[i] 
        #         if profit > 0:
        #             best = max(best, profit)
        # return best

        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit