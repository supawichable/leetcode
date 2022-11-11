'''
383. Ransom Note
https://leetcode.com/problems/ransom-note/
'''


from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteMap = defaultdict(int)
        magazineMap = defaultdict(int)
        for c in magazine:
            magazineMap[c] += 1
        for c in ransomNote:
            ransomNoteMap[c] += 1
            if ransomNoteMap[c] > magazineMap[c]:
                return False
        return True