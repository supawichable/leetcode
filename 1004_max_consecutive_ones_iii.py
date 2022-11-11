'''
1004. Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/
'''


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = curr = 0
        max_size = 0
        for right in range(0, len(nums)):
            if nums[right] == 0:
                curr += 1
            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1
            max_size = max(max_size, right - left + 1)
        return max_size