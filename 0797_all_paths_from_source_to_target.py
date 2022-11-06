'''
797. All Paths From Source to Target
https://leetcode.com/problems/all-paths-from-source-to-target/description/
'''


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def helper(curr):
            if curr[-1] == len(graph) - 1:
                ans.append(curr[:])
            for nxt in graph[curr[-1]]:
                curr.append(nxt)
                helper(curr)
                curr.pop()
        ans = []
        helper([0])
        return ans