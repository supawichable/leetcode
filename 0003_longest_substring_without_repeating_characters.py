'''
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        maxLength = 0
        currLength = 0
        currSub = dict()
        i, j = 0, 0
        while j < len(s):
            if s[j] not in currSub or currSub[s[j]] < i:
                currSub[s[j]] = j
                currLength += 1
                maxLength = max(maxLength, j - i + 1)
            else:
                i = currSub[s[j]] + 1
                currSub[s[j]] = j
            j += 1
        return maxLength
