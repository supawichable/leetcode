'''
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        mem = dict()
        def db(curr):
            if curr == 1:
                return 1
            if curr == 2:
                return 2
            if curr in mem:
                return mem[curr]
            mem[curr] = db(curr-2) + db(curr-1)
            return mem[curr]
        return db(n)