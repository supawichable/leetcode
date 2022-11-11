'''
461. Hamming Distance
https://leetcode.com/problems/hamming-distance/
'''


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x^y
        ans = 0
        while xor:
            ans += 1
            xor = xor & (xor-1)
        return ans


class Solution2:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')