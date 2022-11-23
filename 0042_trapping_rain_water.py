'''
42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/
'''


class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft, maxright = height[0], height[-1]
        left, right = 0, len(height) - 1
        count = 0
        while 0 <= right and left < len(height) and left <= right:
            if height[left] < height[right]:
                left += 1
                maxleft = max(height[left], maxleft)
                if left < right:
                    count += max(maxleft - height[left], 0)
            else:
                right -= 1
                maxright = max(height[right], maxright)
                if left < right:
                    count += max(maxright - height[right], 0)
        return count
