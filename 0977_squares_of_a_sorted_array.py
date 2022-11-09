'''
977. Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/description/
'''


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1
        ans = [0 for _ in range(len(nums))]
        i = len(nums) - 1
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                ans[i] = nums[right] ** 2
                right -= 1
            else:
                ans[i] = nums[left] ** 2
                left += 1
            i -= 1
        return ans
        