'''
223. Rectangle Area
https://leetcode.com/problems/rectangle-area/
'''


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        def axis_overlaps(ax1, ax2, bx1, bx2):
            if ax1 > bx1:
                ax1, bx1 = bx1, ax1
                ax2, bx2 = bx2, ax2
            if bx1 <= ax2:
                return min(ax2, bx2) - bx1
            return 0
        a_area = (ax2 - ax1) * (ay2 - ay1)
        b_area = (bx2 - bx1) * (by2 - by1)
        overlapping = axis_overlaps(ax1, ax2, bx1, bx2) * axis_overlaps(ay1, ay2, by1, by2)
        return a_area + b_area - overlapping
