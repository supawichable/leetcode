'''
35. Search Insert Position
https://leetcode.com/problems/search-insert-position/description/
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid+1
        return left