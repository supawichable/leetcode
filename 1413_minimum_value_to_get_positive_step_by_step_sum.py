'''
1413. Minimum Value to Get Positive Step by Step Sum
https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
'''


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minPrefix = float('inf')
        currSum = 0
        for num in nums:
            currSum += num
            minPrefix = min(currSum, minPrefix)
        return max(1, 1 - minPrefix)