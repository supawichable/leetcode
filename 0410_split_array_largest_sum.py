'''
410. Split Array Largest Sum
https://leetcode.com/problems/split-array-largest-sum/
'''


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def check(max_sum):
            curr_sum = 0
            split_count = 0
            for num in nums:
                curr_sum += num
                if curr_sum > max_sum:
                    curr_sum = num
                    split_count += 1
            return split_count <= k-1
        
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left