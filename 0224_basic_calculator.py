'''
224. Basic Calculator
https://leetcode.com/problems/basic-calculator/
'''


class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        stack = []
        i = 0
        res = 0
        def evaluate():
            nonlocal stack
            ret = 0
            has_pending = False
            pending = 0
            while stack:
                popped = stack.pop()
                if type(popped) == int:
                    pending = popped
                    has_pending = True
                elif popped == "+":
                    ret += pending
                    has_pending = False
                elif popped == "-":
                    ret -= pending
                    has_pending = False
                if popped == '(':
                    if has_pending:
                        ret += pending
                    return ret
            if has_pending:
                ret += pending
            return ret

        while i < len(s):
            if s[i] in ['(', '+', '-']:
                stack.append(s[i])
                i += 1
            elif s[i].isnumeric():
                val = 0
                while i < len(s) and s[i].isnumeric():
                    val *= 10
                    val += int(s[i])
                    i += 1
                stack.append(val)
            elif s[i] == ')':
                stack.append(evaluate())
                i += 1
        return evaluate()
