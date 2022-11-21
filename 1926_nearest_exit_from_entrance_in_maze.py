'''
1926. Nearest Exit From Entrance in Maze
https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
'''


from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n, m = len(maze), len(maze[0])

        def is_exit(cell: List[int]):
            return cell != entrance and \
            maze[cell[0]][cell[1]]== '.' and \
            (cell[0] == 0 or cell[0] == n-1 or cell[1] == 0 or cell[1] == m-1)

        def is_valid(cell: List[int]):
            return 0 <= cell[0] < n and \
            0 <= cell[1] < m and \
            maze[cell[0]][cell[1]] == '.'
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque([entrance])
        seen = set([tuple(entrance)])
        path_len = -1
        while queue:
            len_lvl = len(queue)
            path_len += 1
            for _ in range(len_lvl):
                curr_cell = queue.popleft()
                if is_exit(curr_cell):
                    return path_len
                for d in directions:
                    new_cell = [curr_cell[0] + d[0], curr_cell[1] + d[1]]
                    if tuple(new_cell) not in seen and is_valid(new_cell):
                        seen.add(tuple(new_cell))
                        queue.append(new_cell)
        return -1
