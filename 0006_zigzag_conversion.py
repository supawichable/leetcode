'''
6. Zigzag Conversion
https://leetcode.com/problems/zigzag-conversion/
'''


from collections import defaultdict


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        hashmap = defaultdict(list)
        def down(start):
            for i in range(numRows):
                if start+i >= len(s):
                    return
                hashmap[i].append(s[start+i])
        def up(start):
            for i in range(numRows-2):
                if start + i >= len(s):
                    return
                hashmap[numRows - i - 2].append(s[start + i])
        
        start = 0
        while start < len(s):
            down(start)
            up(start+numRows)
            start += 2 * numRows - 2
        ans = []
        for vals in hashmap.values():
            ans += vals
        return ''.join(ans)
