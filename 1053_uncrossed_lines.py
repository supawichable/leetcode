'''
1035. Uncrossed Lines
https://leetcode.com/problems/uncrossed-lines/
'''


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        rows, cols = len(nums1) + 1, len(nums2) + 1
        dp = [[0 for i in range(cols)] for j in range(rows)]

        for i in range(1, rows):
            for j in range(1, cols):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]
