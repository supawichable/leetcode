'''
1235. Maximum Profit in Job Scheduling
https://leetcode.com/problems/maximum-profit-in-job-scheduling/
'''


import heapq


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        mem = dict()
        jobs = sorted([(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))])
        def dfs(i):
            if i >= len(startTime):
                return 0
            if i in mem:
                return mem[i]
            k = bisect.bisect_left(jobs, jobs[i][1], key = lambda j: j[0])
            mem[i] = max(jobs[i][2] + dfs(k), dfs(i+1))
            return mem[i]
        return dfs(0)

# heap
class Solution2:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted([(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))])
        heap = []
        max_profit = 0
        for start, end, prof in jobs:
            while heap and heap[0][0] <= start:
                max_profit = max(max_profit, heap[0][1])
                heapq.heappop(heap)
            heapq.heappush(heap, (end, prof + max_profit))
        return max([x[1] for x in heap])