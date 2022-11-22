'''
246. Strobogrammatic Number
https://leetcode.com/problems/strobogrammatic-number/
'''


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        s = str(num)
        left, right = 0, len(s) - 1
        can_flip = set(['0', '1', '8'])
        while left <= right:
            if (s[left] == '6' and s[right] == '9') or \
            (s[left] == '9' and s[right] == '6') or \
            (s[left] == s[right] and s[right] in can_flip):
                left += 1
                right -= 1
            else:
                return False
        return True
