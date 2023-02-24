'''
159. Longest Substring with At Most Two Distinct Characters
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
'''


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left, right = 0, 0
        distinct_chars = dict()
        max_len = 0
        n = len(s)
        while right < n:
            distinct_chars[s[right]] = right
            if len(distinct_chars) <= 2:
                max_len = max(max_len, right - left + 1)
                right += 1
            else:
                if distinct_chars[s[left]] == left:
                    del distinct_chars[s[left]]
                left += 1
        return max_len
                
