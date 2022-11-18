'''
15. 3Sum
https://leetcode.com/problems/3sum/
'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums, target, ans):
            mem = dict()
            for i, n in enumerate(nums):
                if target - n in mem:
                    ans.add(tuple(sorted((-target, target - n, n))))
                mem[n] = i
        ans = set()
        for i, num in enumerate(nums):
            twoSum(nums[i+1:], -num, ans)
        return [list(x) for x in ans]
