'''
31. Next Permutation
https://leetcode.com/problems/next-permutation/
'''


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        stack = []
        popped = []
        isPopped = False
        for i in range(len(nums) - 1, -1, -1):
            j = i + 1
            while j < len(nums) and nums[i] < nums[j]:
                isPopped = True
                j += 1
            if isPopped:
                tmp1 = nums[j - 1]
                tmp2 = nums[j:][::-1]
                tmp3 = nums[i]
                tmp4 = nums[i+1:j-1][::-1]         
                len_j = len(nums) - j
                nums[i] = tmp1
                nums[i+1:i+len_j+1] = tmp2
                nums[i+len_j+1] = tmp3
                if i+len_j+2 < len(nums):
                    nums[i+len_j+2:len(nums)] = tmp4
                break
            else:
                stack.append(nums[i])
        if not isPopped:
            nums.reverse()
