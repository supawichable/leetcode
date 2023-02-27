'''
849. Maximize Distance to Closest Person
https://leetcode.com/problems/maximize-distance-to-closest-person/
'''


import math


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        empty_count = 0
        max_empty = 0
        i = 0
        while i < n and not seats[i]:
            i += 1
        for s in seats[i:]:
            if s == 0:
                empty_count += 1
            else:
                max_empty = max(empty_count, max_empty)
                empty_count = 0
        max_empty = max(i,empty_count, math.ceil(max_empty/2))
        return max_empty
