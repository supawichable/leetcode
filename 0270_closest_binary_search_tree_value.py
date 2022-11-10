'''
270. Closest Binary Search Tree Value
https://leetcode.com/problems/closest-binary-search-tree-value/
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root.left and not root.right:
            return root.val
        closestValueNext = float('inf')
        if target > root.val:
            if root.right:
                closestValueNext = self.closestValue(root.right, target)
        else:
            if root.left:
                closestValueNext = self.closestValue(root.left, target)
        return root.val if abs(target-closestValueNext) > abs(target-root.val) else closestValueNext