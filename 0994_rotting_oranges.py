'''
994. Rotting Oranges
https://leetcode.com/problems/rotting-oranges/
'''


from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh_oranges = 0
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1
        if not fresh_oranges:
            return 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        count = 0
        while queue and fresh_oranges:
            lvl_len = len(queue)
            count += 1
            for _ in range(lvl_len):
                (x, y) = queue.popleft()
                for dx, dy in dirs:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 1:
                        queue.append((new_x, new_y))
                        fresh_oranges -= 1
                        grid[new_x][new_y] = 2
        return -1 if fresh_oranges else count
