'''
263. Ugly Number
https://leetcode.com/problems/ugly-number/
'''


class Solution:
    def isUgly(self, n: int) -> bool:
        def divide_until_end(n, divider):
            while n != 0 and n % divider == 0:
                n /= divider
            return n

        for d in [5, 3, 2]:
            n = divide_until_end(n ,d)
        return n == 1
