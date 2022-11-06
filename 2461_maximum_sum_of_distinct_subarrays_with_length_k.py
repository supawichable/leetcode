'''
2461. Maximum Sum of Distinct Subarrays With Length K
https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
'''


from collections import Counter


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        i, j = 0, k-1
        curr_sum = sum(nums[:k])
        counter = Counter(nums[:k])
        while j < len(nums):
            if i != 0:
                curr_sum += -nums[i-1] + nums[j]
                if counter[nums[i-1]] == 1:
                    del counter[nums[i-1]]
                else:
                    counter[nums[i-1]] -= 1
                if nums[j] in counter:
                    counter[nums[j]] += 1
                else:
                    counter[nums[j]] = 1
            if len(counter) == j+1-i:
                max_sum = max(curr_sum, max_sum)
            i += 1
            j += 1
        return max_sum