class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            if len(prices) < 2:
                return 0
            min_so_far = prices[0]
            max_profit = 0
            for price in prices[1:]:
                profit = price - min_so_far
                if min_so_far > price:
                    min_so_far = price
                if profit > max_profit:
                    max_profit = profit
            return max_profit