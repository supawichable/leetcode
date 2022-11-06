'''
967. Numbers With Same Consecutive Differences
https://leetcode.com/problems/numbers-with-same-consecutive-differences/
'''


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def backtrack(curr):
            if len(curr) == n:
                ans.append(''.join(curr))
                return
            last_digit = int(curr[-1])
            for nxt in [last_digit + k, last_digit - k]:
                if 0 <= nxt <= 9:
                    curr.append(str(nxt))
                    backtrack(curr)
                    curr.pop()
        ans = []
        for i in range(1, 10):
            backtrack([str(i)])
        return list(set(ans))