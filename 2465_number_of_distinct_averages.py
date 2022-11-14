'''
2465. Number of Distinct Averages
https://leetcode.com/problems/number-of-distinct-averages/
'''


import heapq


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        distinctAvg = set()
        minHeap = nums.copy()
        maxHeap = [-num for num in nums]
        heapq.heapify(minHeap)
        heapq.heapify(maxHeap)
        for i in range(len(nums)//2):
            distinctAvg.add((heapq.heappop(minHeap) - heapq.heappop(maxHeap))/2)
        return len(distinctAvg)
