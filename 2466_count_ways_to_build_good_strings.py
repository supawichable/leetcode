'''
2466. Count Ways to Build Good Strings
https://leetcode.com/problems/count-ways-to-build-good-strings/
'''


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mem = dict()
        def dp(curr):
            if curr < 0:
                return 0
            if curr == 0:
                return 1
            if curr in mem:
                return mem[curr]
            mem[curr] = (dp(curr-zero) + dp(curr-one))
            return mem[curr] % (10**9 + 7)
        ans = 0
        for i in range(low, high+1):
            ans += dp(i)
        return ans % (10**9 + 7)
