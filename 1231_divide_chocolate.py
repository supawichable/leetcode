'''
1231. Divide Chocolate
https://leetcode.com/problems/divide-chocolate/
'''

class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def check(min_sweet):
            sum_now = 0
            count = 0
            for p in sweetness:
                sum_now += p
                if sum_now >= min_sweet:
                    sum_now = 0
                    count += 1
            return count < k+1
                    
        left, right = min(sweetness), sum(sweetness) // (k+1) + 1
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left - 1