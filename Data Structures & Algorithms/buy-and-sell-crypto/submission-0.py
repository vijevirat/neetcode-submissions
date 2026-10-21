class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = float('inf')
        sell = float('-inf')
        i = 0
        while i < len(prices):
            buy = min(buy, prices[i])
            j = i +1
            while j < len(prices) and prices[j] >= prices[j-1]:
                j+=1
            sell = prices[j-1]
            i = j
            profit = max(profit, (sell-buy))
        return profit
        