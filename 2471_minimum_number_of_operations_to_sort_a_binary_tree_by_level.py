'''
2471. Minimum Number of Operations to Sort a Binary Tree by Level
https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/
'''


from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:

        # return minimum number of operations required to sort array
        def count_operations(arr):
            idx_arr = {c: i for i, c in enumerate(arr)}
            count = 0
            for i_sorted, c in enumerate(sorted(arr)):
                i = idx_arr[c]
                # if c is not in the right position, swap it with the value in its right position
                if i != i_sorted:
                    count += 1
                    arr[i_sorted], arr[i] = arr[i], arr[i_sorted] 
                    idx_arr[arr[i]] = i
                    idx_arr[arr[i_sorted]] = i_sorted
            return count

        queue = deque([root])
        ans = 0

        # BFS to calculate minimum number of operations per level
        while queue:
            curr_level_len = len(queue)
            curr_level_val = []
            for _ in range(curr_level_len):
                curr_node = queue.popleft()
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
                curr_level_val.append(curr_node.val)
            ans += count_operations(curr_level_val)
            
        return ans
