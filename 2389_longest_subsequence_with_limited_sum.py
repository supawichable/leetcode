'''
2389. Longest Subsequence With Limited Sum
https://leetcode.com/problems/longest-subsequence-with-limited-sum/description/
'''

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        sums = []
        curr_sum = 0
        for num in nums:
            curr_sum += num
            sums.append(curr_sum)

        def search(query):
            left, right = 0, len(nums)
            while left < right:
                mid  = (left + right) // 2
                if query < sums[mid]:
                    right = mid
                else:
                    left = mid+1
            return left

        return [search(q) for q in queries]
        