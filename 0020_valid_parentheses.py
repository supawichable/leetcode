'''
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
'''


class Solution:
    def isValid(self, s: str) -> bool:
        def isPair(c1, c2):
            return (c1 == '(' and c2 == ')') or \
                (c1 == '[' and c2 == ']') or \
                (c1 == '{' and c2 == '}')
        stack = []
        for c in s:
            if not stack or not isPair(stack[-1], c):
                if c in '])}':
                    return False
                else:
                    stack.append(c)
            else:
                stack.pop()
        return False if stack else True
