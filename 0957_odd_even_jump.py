'''
957. Odd Even Jump
https://leetcode.com/problems/odd-even-jump/
'''


class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        def nextGreater(idx_arr):
            stack = []
            ret = [None] * len(idx_arr)
            for i, a in enumerate(idx_arr):
                while stack and idx_arr[stack[-1]] < a:
                    ret[idx_arr[stack.pop()]] = a
                stack.append(i)
            return ret
        n = len(arr)
        idx_sorted = sorted(range(n), key = lambda x:arr[x])
        odd = nextGreater(idx_sorted)
        idx_sorted.sort(key=lambda x: arr[x], reverse=True)
        even = nextGreater(idx_sorted)
        dp = [[0, 0] for _ in range(n)]
        dp[-1] = [1, 1]
        for i in range(n-2, -1, -1):
            dp[i][0] = dp[odd[i]][1] if odd[i] else 0
            dp[i][1] = dp[even[i]][0] if even[i] else 0
        return sum([dp[i][0] for i in range(n)])
