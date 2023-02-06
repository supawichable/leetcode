'''
16. 3sum Closestsolutions
https://leetcode.com/problems/3sum-closest/
'''


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float('inf')
        nums.sort()
        for i, num in enumerate(nums):
            res = self.twoSum(nums, i, target, res)
        return res

    def twoSum(self, nums, idx, target, res):
        lo, hi = idx + 1, len(nums) - 1
        while lo < hi:
            summ = nums[idx] + nums[lo] + nums[hi]
            if abs(summ - target) < abs(res - target):
                res = summ
            if summ < target:
                lo += 1
            else:
                hi -= 1
        return res
