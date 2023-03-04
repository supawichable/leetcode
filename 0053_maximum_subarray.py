'''
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_nums = max(nums)
        if max_nums <= 0:
            return max_nums

        largest = nums[0]
        right = 0
        curr = nums[0]
        n = len(nums)

        prev = 0
        while right < n:
            left = right
            curr, between = 0, 0
            while left < n and nums[left] <= 0:
                between += nums[left]
                left += 1
            prev += between
            right = left
            while right < n and nums[right] >= 0:
                curr += nums[right]
                right += 1
            if prev > 0:
                curr += prev
            prev = curr
            largest = max(largest, curr)

        return largest
