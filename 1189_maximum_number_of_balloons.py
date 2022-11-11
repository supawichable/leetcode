'''
1189. Maximum Number of Balloons
https://leetcode.com/problems/maximum-number-of-balloons/
'''


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = dict()
        for c in 'balloon':
            counter[c] = 0
        for c in text:
            if c in counter:
                counter[c] += 1
        counter['l'] //= 2
        counter['o'] //= 2
        return min(counter.values())
        