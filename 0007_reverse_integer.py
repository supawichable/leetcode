'''
7. Reverse Integer
https://leetcode.com/problems/reverse-integer/
'''


class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        is_neg = False
        if x < 0:
            is_neg = True
            x = -x
        while x:
            rev *= 10
            rev += x % 10
            x //= 10
        if rev > 2**31-1:
            return 0
        return -rev if is_neg else rev
