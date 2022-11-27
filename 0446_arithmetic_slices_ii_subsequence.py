'''
446. Arithmetic Slices Ii Subsequence
https://leetcode.com/problems/arithmetic-slices-ii-subsequence/
'''


from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        mem = [defaultdict(int) for _ in range(len(nums))]
        ans = 0
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                mem[i][diff] += (1 + mem[j][diff])
                ans += mem[j][diff]
        return ans
