'''
1099. Two Sum Less Than K
https://leetcode.com/problems/two-sum-less-than-k/
'''


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return -1
        sorted_nums = sorted(nums)
        left, right = 0, len(nums) - 1
        max_sum = -1
        while left < right:
            curr_sum = sorted_nums[left] + sorted_nums[right]
            if curr_sum < k:
                max_sum = max(max_sum, curr_sum)
                left += 1
            else:
                right -= 1
        return max_sum
