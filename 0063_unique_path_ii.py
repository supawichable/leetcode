'''
63. Unique Paths II
https://leetcode.com/problems/unique-paths-ii/
'''


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1        
        if obstacleGrid[m][n]:
            return 0
        mem = dict()
        def dp(row, col):
            if row + col == 0:
                mem[(row, col)] = 1
                return 1
            if (row, col) in mem:
                return mem[(row, col)]
            ans = 0
            if row - 1 >= 0 and obstacleGrid[row - 1][col] == 0:
                ans += dp(row-1, col)
            if col - 1 >= 0 and obstacleGrid[row][col - 1] == 0:
                ans += dp(row, col-1)
            mem[(row, col)] = ans
            return ans
        return dp(m, n)