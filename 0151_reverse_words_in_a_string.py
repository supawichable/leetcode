'''
151. Reverse Words in a String
https://leetcode.com/problems/reverse-words-in-a-string/
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        split = s.split()
        return ' '.join([split[i] for i in range(len(split)-1, -1, -1)])