'''
1196. How Many Apples Can You Put into the Basket
https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/
'''


import heapq


class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight_limit = 5000
        sum_weight = 0
        num_apples = 0
        heapq.heapify(weight)
        while weight and sum_weight + weight[0] <= weight_limit:
            sum_weight += heapq.heappop(weight)
            num_apples += 1
        return num_apples