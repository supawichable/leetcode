'''
746. Min Cost Climbing Stairs
https://leetcode.com/problems/min-cost-climbing-stairs/
'''


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mem = dict()
        def dp(curr):
            if curr < 2:
                return 0
            if curr in mem:
                return mem[curr]
            mem[curr] = min(dp(curr-1) + cost[curr-1], dp(curr-2) + cost[curr-2])
            return mem[curr]
        return dp(len(cost))