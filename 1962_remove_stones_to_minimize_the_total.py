'''
1962. Remove Stones to Minimize the Total
https://leetcode.com/problems/remove-stones-to-minimize-the-total/
'''

import heapq


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles_processed = [-pile for pile in piles]
        heapq.heapify(piles_processed)
        for _ in range(k):
            removed = -heapq.heappop(piles_processed)
            heapq.heappush(piles_processed, -(removed - removed//2))
        return -sum(piles_processed)