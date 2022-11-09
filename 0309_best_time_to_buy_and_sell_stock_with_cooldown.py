'''
309. Best Time to Buy and Sell Stock with Cooldown
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
'''

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        mem = dict()
        def dp(i, holding):
            if (i, holding) in mem:
                return mem[(i, holding)]
            if i >= len(prices):
                mem[(i, holding)] = 0
                return 0
            ans = dp(i+1, holding)
            if holding:
                ans = max(ans, dp(i+1, False) + prices[i] - fee)
            else:
                ans = max(ans, dp(i+1, True) - prices[i])
            mem[(i, holding)] = ans
            return ans
        return dp(0, False)