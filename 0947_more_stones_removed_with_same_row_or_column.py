'''
947. Most Stones Removed with Same Row or Column
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
'''


from collections import defaultdict


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = defaultdict(list)
        for s in stones:
            graph[(s[0], -1)].append(s)
            graph[(-1, s[1])].append(s)
        
        seen = set()
        def bfs(starter):
            queue = deque([starter])
            while queue:
                level_len = len(queue)
                for _ in range(level_len):
                    curr = queue.popleft()
                    for nxt in [x for x in graph[(curr[0], -1)]+graph[(-1, curr[1])] if tuple(x) not in seen]:
                        seen.add(tuple(nxt))
                        queue.append(nxt)
        count = 0
        for stone in stones:
            if len(seen) == len(stones):
                break
            if tuple(stone) not in seen:
                count += 1
                bfs(stone)
        return len(stones) - count