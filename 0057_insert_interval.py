'''
57. Insert Interval
https://leetcode.com/problems/insert-interval/
'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        for interval in intervals:
            if interval[1] < newInterval[0]:
                ans.append(interval)
            elif newInterval[1] < interval[0]:
                ans.append(newInterval)
                newInterval = interval
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        ans.append(newInterval)
        return ans
