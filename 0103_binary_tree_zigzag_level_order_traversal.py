'''
103. Binary Tree Zigzag Level Order Traversal
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
'''


from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        ans = []
        queue = deque([root])
        lvl = 0
        while queue:
            lvl += 1
            lvl_ans = []
            lvl_len = len(queue)
            for _ in range(lvl_len):
                curr_node = queue.popleft()
                lvl_ans.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            if lvl % 2 == 0:
                lvl_ans.reverse()
            ans.append(lvl_ans)

        return ans
