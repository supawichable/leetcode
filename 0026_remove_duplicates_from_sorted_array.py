'''
26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = -101
        fast, slow = 0, -1
        while fast < len(nums):
            if nums[fast] != prev:
                slow += 1
                nums[slow] = nums[fast]
            prev = nums[fast]
            fast += 1
        return slow + 1