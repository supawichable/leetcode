'''
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/
'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first, last = strs[0], strs[-1]
        i = 0
        while i < (min(len(first), len(last))) and first[i] == last[i]:
            i += 1
        return first[:i]
