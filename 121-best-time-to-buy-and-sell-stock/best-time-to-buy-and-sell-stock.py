class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            profit = max(prices[i] - mini,profit)
            mini = min(mini,prices[i])
        return profit