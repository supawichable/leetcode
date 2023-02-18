'''
55. Jump Game
https://leetcode.com/problems/jump-game/
'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        i, j = n-2, n-1
        while i >= 0:
            if i + nums[i] >= j:
                j = i
            i -= 1
        return j == 0
