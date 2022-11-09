'''
931. Minimum Falling Path Sum
https://leetcode.com/problems/minimum-falling-path-sum/
'''


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        mem = dict()
        def dp(row, col):
            if row == 0:
                return matrix[row][col]
            if (row, col) in mem:
                return mem[(row, col)]
            ans = float('inf')
            if col - 1 >= 0:
                ans = min(ans, dp(row-1, col-1))
            if col + 1 < n:
                ans = min(ans, dp(row-1, col+1))
            ans = min(ans, dp(row-1, col)) + matrix[row][col]
            mem[(row, col)] = ans
            return ans
        return min([dp(m-1, x) for x in range(n)])