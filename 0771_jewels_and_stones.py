'''
771. Jewels and Stones
https://leetcode.com/problems/jewels-and-stones/
'''


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)
        count = 0
        for c in stones:
            if c in jewels_set:
                count += 1
        return count