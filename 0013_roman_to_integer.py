'''
13. Roman to Integer
https://leetcode.com/problems/roman-to-integer/
'''


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }

        curr_sum = 0
        for i, c in enumerate(s):
            if i + 1 < len(s):
                if (c == 'I' and s[i+1] in ['V', 'X']) or \
                (c == 'X' and s[i+1] in ['L', 'C']) or \
                (c == 'C' and s[i+1] in ['D', 'M']):
                    curr_sum -= roman_dict[c]
                    continue
            curr_sum += roman_dict[c]
        return curr_sum
