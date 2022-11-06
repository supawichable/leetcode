'''
216. Combination Sum III
https://leetcode.com/problems/combination-sum-iii/
'''


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(curr, curr_sum):
            if len(curr) == k:
                if curr_sum == n:
                    ans.append(curr[:])
                return
            for i in range(curr[-1] + 1, 10):
                if curr_sum + i <= n and i not in curr:
                    curr.append(i)
                    backtrack(curr, curr_sum + i)
                    curr.pop()
                    
        ans = []
        for i in range(1, 10):
            backtrack([i], i)
        return ans