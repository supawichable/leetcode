'''
163. Missing Ranges
https://leetcode.com/problems/missing-ranges/
'''


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        def addToOut(out, left_val, right_val):
            diff = right_val - left_val
            if diff > 2:
                out.append(f'{str(left_val+1)}->{str(right_val-1)}')
            elif diff == 2:
                out.append(f'{str(left_val+1)}')

        out = []
        if len(nums) == 0:
            addToOut(out, lower-1, upper+1)
            return out
        elif len(nums) == 1:
            addToOut(out, lower-1, nums[0])
            addToOut(out, nums[0], upper+1)
            return out
        left, right = 0, 1
        addToOut(out, lower-1, nums[left])
        while right < len(nums):
            addToOut(out, nums[left], nums[right])
            left += 1
            right += 1
        addToOut(out, nums[left], upper+1)
        return out
