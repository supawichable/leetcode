'''
22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/
'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(curr, opens, closes):
            if closes == n:
                ans.append(''.join(curr))
                return
            if opens < n:
                curr.append('(')
                backtrack(curr, opens+1, closes)
                curr.pop()
            if closes < opens:
                curr.append(')')
                backtrack(curr, opens, closes+1)
                curr.pop()

        ans = []
        backtrack([], 0, 0)
        return ans