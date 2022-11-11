'''
1426. Counting Elements
https://leetcode.com/problems/counting-elements/
'''


class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr_set = set(arr)
        count = 0
        for a in arr:
            if a+1 in arr_set:
                count += 1
        return count