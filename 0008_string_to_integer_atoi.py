'''
8. String to Integer Atoi
https://leetcode.com/problems/string-to-integer-atoi/
'''


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0

        is_neg = False
        if s[0] in ['+', '-']:
            is_neg = s[0] == '-'
            s = s[1:]
        if len(s) == 0 or not s[0].isnumeric():
            return 0

        i = 0
        while i < len(s) and s[i].isnumeric():
            i += 1
        s_int = int(s[:i])
        if is_neg:
            s_int = -s_int

        two_31 = 2 ** 31
        if s_int < -two_31:
            return -two_31
        if s_int > two_31 - 1:
            return two_31 - 1
        return s_int
            
