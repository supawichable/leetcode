'''
15. 3Sum
https://leetcode.com/problems/3sum/
'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            if i == 0 or nums[i] != nums[i-1]:
                self.twoSum(nums, i, -num, res)
        return res


    def twoSum(self, nums, idx, target, res):
        lo, hi = idx + 1, len(nums) - 1
        while lo < hi:
            summ = nums[lo] + nums[hi]
            if summ > target:
                hi -= 1
            elif summ < target:
                lo += 1
            else:
                res.append([-target, nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo-1]:
                    lo += 1
