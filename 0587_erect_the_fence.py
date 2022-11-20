'''
587. Erect the Fence
https://leetcode.com/problems/erect-the-fence/
'''


class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:

        def cross(p1, p2, p3):
            p12 = [p2[0] - p1[0], p2[1] - p1[1]]
            p23 = [p3[0] - p2[0], p3[1] - p2[1]]
            return p12[0] * p23[1] - p12[1] * p23[0]
        
        def add_to_stack(stack, arr):
            for p in arr:
                while len(stack) >= 2 and cross(stack[-2], stack[-1], p) > 0:
                    stack.pop()
                stack.append(tuple(p))

        if len(points) <= 2:
            return points
        left_sorted = sorted(points)
        right_sorted = left_sorted[::-1]
        stack = [tuple(left_sorted[0]), tuple(left_sorted[1])]
        add_to_stack(stack, left_sorted[2:])
        add_to_stack(stack, right_sorted)
        return list(set(stack))

