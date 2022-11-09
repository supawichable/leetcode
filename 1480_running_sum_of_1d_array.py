'''
1480. Running Sum of 1d Array
https://leetcode.com/problems/running-sum-of-1d-array/
'''


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        currSum = 0
        for num in nums:
            currSum += num
            runningSum.append(currSum)
        return runningSum