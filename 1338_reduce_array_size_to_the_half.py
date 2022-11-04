'''
1338. Reduce Array Size to The Half
https://leetcode.com/problems/reduce-array-size-to-the-half/
'''


from collections import Counter
import heapq


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        heap = [-x for x in Counter(arr).values()]
        removed, removed_sets = 0, 0
        heapq.heapify(heap)
        while heap and removed < len(arr)/2:
            removed -= heapq.heappop(heap)
            removed_sets += 1
        return removed_sets
