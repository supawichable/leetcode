'''
43. Multiply Strings
https://leetcode.com/problems/multiply-strings/
'''


from collections import defaultdict


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        intmap = {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '0': 0
        }
        charmap = {
            1: '1',
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
            0: '0'
        }
        if num1 == '0' or num2 == '0':
            return '0'
        res = defaultdict(int)
        ret = []
        len1, len2 = len(num1), len(num2)
        for i, c1 in enumerate(num1[::-1]):
            for j, c2 in enumerate(num2[::-1]):
                res[i + j] += intmap[c1] * intmap[c2]
        for i in range(len1 + len2):
            ret.append(charmap[res[i] % 10])
            if res[i] // 10:
                res[i+1] += res[i] // 10
        i = len(ret) - 1
        while ret[i] == '0':
            i -= 1
        ret = ret[:i+1]
        ret.reverse()
        return ''.join(ret)
