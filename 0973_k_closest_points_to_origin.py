'''
973. K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/
'''


import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for point in points:
            heapq.heappush(heap, (-(point[0]**2 + point[1]**2), point))
            if len(heap) > k:
                heapq.heappop(heap)
        return [item[1] for item in heap]