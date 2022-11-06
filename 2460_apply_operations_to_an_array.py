'''
2460. Apply Operations to an Array
https://leetcode.com/problems/apply-operations-to-an-array/
'''


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            if i == len(nums) - 1:
                break
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        ans = []
        zero_count = 0
        for num in nums:
            if num != 0:
                ans.append(num)
            else:
                zero_count += 1
        for _ in range(zero_count):
            ans.append(0)
        return ans