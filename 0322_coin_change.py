'''
322. Coin Change
https://leetcode.com/problems/coin-change/
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = dict()
        def dp(curr):
            if curr < 0:
                return -1
            if curr == 0:
                return 0
            if curr in mem:
                return mem[curr]
            ans = curr+1
            for c in coins:
                dp_ret = dp(curr-c)
                if dp_ret != -1:
                    ans = min(ans, dp_ret + 1)
            if ans == curr+1:
                mem[curr] = -1
                return -1
            mem[curr] = ans
            return ans
        return dp(amount)
            