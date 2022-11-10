'''
1971. Find if Path Exists in Graph
https://leetcode.com/problems/find-if-path-exists-in-graph/
'''


from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        seen = set()
        def dfs(i):
            if i == destination:
                return True
            for v in graph[i]:
                if (i, v) not in seen and (v, i) not in seen:
                    seen.add((i, v))
                    if dfs(v):
                        return True
            return False
        return dfs(source)           