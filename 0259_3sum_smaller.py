'''
259. 3sum Smaller
https://leetcode.com/problems/3sum-smaller/
'''


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        count = 0
        nums.sort()
        for i, num in enumerate(nums):
            count += self.twoSum(nums, i, target-num)
        return count

    def twoSum(self, nums, idx, target):
        lo, hi = idx + 1, len(nums) - 1
        count = 0
        while lo < hi:
            summ = nums[lo] + nums[hi]
            if summ >= target:
                hi -= 1
            else:
                count += hi - lo
                lo += 1
        return count
