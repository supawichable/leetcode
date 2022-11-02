'''
1167. Minimum Cost to Connect Sticks
https://leetcode.com/problems/minimum-cost-to-connect-sticks/
'''


import heapq


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        cost = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            popped1 = heapq.heappop(sticks)
            popped2 = heapq.heappop(sticks)
            heapq.heappush(sticks, popped1+popped2)
            cost += popped1+popped2
        return cost