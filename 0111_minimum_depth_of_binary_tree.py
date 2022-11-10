'''
111. Minimum Depth of Binary Tree
https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(curr, count):
            nonlocal min_path
            ret = float('inf')
            if curr.left == None and curr.right == None:
                ret = count
            if curr.left:
                ret = min(ret, dfs(curr.left, count+1))
            if curr.right:
                ret = min(ret, dfs(curr.right, count+1))
            min_path = min(min_path, ret)
            return ret
        min_path = float('inf')
        dfs(root, 1)
        return min_path