'''
10. Regular Expression Matching
https://leetcode.com/problems/regular-expression-matching/
'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        mem = dict()
        def dp(s_idx, p_idx):
            if (s_idx, p_idx) in mem:
                return mem[(s_idx, p_idx)]
            if s_idx == len(s):
                if p_idx >= len(p):
                    mem[(s_idx, p_idx)] = True
                elif p_idx + 1 < len(p) and p[p_idx + 1] == "*":
                    mem[(s_idx, p_idx)] = dp(s_idx, p_idx + 2)
                else:
                    mem[(s_idx, p_idx)] = False
            else:
                if p_idx >= len(p):
                    mem[(s_idx, p_idx)] = False
                elif p[p_idx] == s[s_idx] or p[p_idx] == '.':
                    if p_idx + 1 < len(p) and p[p_idx + 1] == "*":
                        mem[(s_idx, p_idx)] = dp(s_idx + 1, p_idx) or dp(s_idx, p_idx + 2)
                    else:
                        mem[(s_idx, p_idx)] = dp(s_idx + 1, p_idx + 1)
                else:
                    if p_idx + 1 < len(p) and p[p_idx + 1] == "*":
                        mem[(s_idx, p_idx)] = dp(s_idx, p_idx + 2)
                    else:
                        mem[(s_idx, p_idx)] = False
            return mem[(s_idx, p_idx)]
        ret = dp(0, 0)
        return ret
