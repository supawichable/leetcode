'''
973. K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/
'''


import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for i, p in enumerate(points):
            heapq.heappush(heap, ((-(p[0] ** 2 + p[1] ** 2)), i))
            if len(heap) > k:
                heapq.heappop(heap)
        return [points[x[1]] for x in heap]


class Solution2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = lambda point: point[0]**2 + point[1]**2)
        return points[:k]