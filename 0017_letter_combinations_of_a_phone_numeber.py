'''
17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
'''


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def backtrack(curr):
            if len(curr) == len(digits):
                ans.append(''.join(curr))
                return
            for c in digit_map[digits[len(curr)]]:
                curr.append(c)
                backtrack(curr)
                curr.pop()
        
        ans = []
        backtrack([])
        return ans            