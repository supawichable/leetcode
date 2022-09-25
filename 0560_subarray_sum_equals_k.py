'''
560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/
'''


from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        total_sum = 0
        count = 0
        hashmap = defaultdict(lambda: 0)
        hashmap[0] = 1
        for i in range(n):
            total_sum += nums[i]
            if total_sum - k in hashmap:
                count += hashmap[total_sum - k]
            hashmap[total_sum] += 1
        return count
