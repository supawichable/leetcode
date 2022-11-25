'''
907. Sum of Subarray Minimums
https://leetcode.com/problems/sum-of-subarray-minimums/
'''


class Solution1:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        minsum = 0
        stack = []

        for i in range(len(arr) + 1):
            while stack and (i == len(arr) or arr[i] <= arr[stack[-1]]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                minsum += arr[mid] * (i - mid) * (mid - left)
            stack.append(i)
        
        return minsum % MOD


class Solution2:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        minsum = 0
        stack = []
        dp = [0] * len(arr)

        for i in range(len(arr)):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop() 
            if stack:
                prev_smaller = stack[-1]
                dp[i] = dp[prev_smaller] + (i - prev_smaller) * arr[i]
            else:
                dp[i] = (i + 1) * arr[i]
            stack.append(i)
        return sum(dp) % MOD
                