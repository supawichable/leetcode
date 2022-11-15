'''
222. Count Complete Tree Nodes
https://leetcode.com/problems/count-complete-tree-nodes/
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def exists(idx, level):        
            tmp = root
            left, right = 0, 2 ** level-1
            for _ in range(level):
                if not tmp:
                    break
                mid = (left + right) // 2
                if idx <= mid:
                    right = mid
                    tmp = tmp.left
                else:
                    left = mid + 1
                    tmp = tmp.right
            return True if tmp else False

        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        tmp = root
        level = -1
        while tmp:
            level += 1
            tmp = tmp.left
        left, right = 1, 2 ** level
        while left < right:
            mid = (left + right) // 2
            if not exists(mid, level):
                right = mid
            else:
                left = mid + 1
        return 2 ** (level) + (left - 1)
