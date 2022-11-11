'''
643. Maximum Average Subarray I
https://leetcode.com/problems/maximum-average-subarray-i/
'''


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        ans_sum = curr_sum
        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i-k]
            ans_sum = max(ans_sum, curr_sum)
        return ans_sum / k