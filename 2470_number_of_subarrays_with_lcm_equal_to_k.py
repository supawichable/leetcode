'''
2470. Number of Subarrays with LCM Equal to K
https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/
'''


import math


class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        ans = 0
        for left in range(len(nums)):
            lcm = nums[left]
            for right in range(left, len(nums)):
                lcm = math.lcm(lcm, nums[right])
                if lcm == k:
                    ans += 1
                elif lcm > k:
                    break
        return ans
