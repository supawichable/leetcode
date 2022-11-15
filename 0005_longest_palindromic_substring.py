'''
5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len_start, max_len = 0, 1
        for i in range(len(s)):
            right = i
            while right < len(s) and s[right] == s[i]:
                right += 1
            left = i - 1
            palindrome_len = right - i
            palindrome_start = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                palindrome_len = right - left + 1
                palindrome_start = left
                left -= 1
                right += 1
            if palindrome_len > max_len:
                max_len = palindrome_len
                max_len_start = palindrome_start
        return s[max_len_start: max_len_start + max_len]
