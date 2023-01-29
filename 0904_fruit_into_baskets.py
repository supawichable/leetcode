'''
904. Fruit Into Baskets
https://leetcode.com/problems/fruit-into-baskets/
'''


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start, end = 0, 0
        picked = {}
        fruit_count = 0
        max_fruit = -float('inf')
        while start <= end and end < len(fruits):
            if fruits[end] in picked:
                picked[fruits[end]] += 1
            else:
                while start < end and len(picked) >= 2:
                    picked[fruits[start]] -= 1
                    if not picked[fruits[start]]:
                        del picked[fruits[start]]
                    start += 1
                picked[fruits[end]] = 1
            fruit_count = end - start + 1
            max_fruit = max(fruit_count, max_fruit)
            end += 1
        return max_fruit
