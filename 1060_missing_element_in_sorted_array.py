'''
1060. Missing Element in Sorted Array
https://leetcode.com/problems/missing-element-in-sorted-array/
'''

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        lenNum = len(nums)
        missing = lambda idx: nums[idx] - nums[0] - idx
        if k > missing(lenNum-1):
            return nums[lenNum - 1] + (k - missing(lenNum-1))
        
        left, right = 0, lenNum - 1
        while left != right:
            pivot = left + (right - left) // 2
            
            if missing(pivot) < k:
                left = pivot + 1
            else:
                right = pivot
        
        return nums[left - 1] + k - missing(left - 1)