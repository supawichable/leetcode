'''
200. Number of Islands
https://leetcode.com/problems/number-of-islands/
'''


from collections import deque
from itertools import product


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        seen = set()
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(x, y):
            queue = deque([(x, y)])
            while queue:
                lvl_len = len(queue)
                for _ in range(lvl_len):
                    curr = queue.popleft()
                    for d in dirs:
                        new_x = curr[0] + d[0]
                        new_y = curr[1] + d[1]
                        if 0 <= new_x < m and 0 <= new_y < n and \
                        (new_x, new_y) not in seen and \
                        grid[new_x][new_y] == '1':
                            seen.add((new_x, new_y))
                            queue.append((new_x, new_y))
            
        
        for i, j in product(range(m), range(n)):
            if (i, j) not in seen and grid[i][j] == '1':
                count += 1
                bfs(i, j)

        return count
