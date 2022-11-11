'''
268. Missing Number
https://leetcode.com/problems/missing-number/
'''


class Solution:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            print(i, num, i^num)
            missing ^= i ^ num
        return missing
