'''
482. License Key Formatting
https://leetcode.com/problems/license-key-formatting/
'''


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '')
        s = s.upper()
        remainder = len(s) % k
        ans = []
        if remainder:
            ans.append(s[:remainder])
        res = [s[k*i + remainder: k*(i+1) + remainder] for i in range(len(s)//k)]
        ans += res
        return '-'.join(ans)
