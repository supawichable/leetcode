'''
79. Word Search
https://leetcode.com/problems/word-search/
'''


from collections import Counter


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, idx):
            if not 0 <= x < m or \
            not 0 <= y < n or \
            board[x][y] != word[idx]:
                return False
            if idx == len(word) - 1:
                return True
            board[x][y] = '#'
            ret = any(dfs(x + d[0], y + d[1], idx+1) for d in directions)
            board[x][y] = word[idx]
            return ret

        m, n = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        if len(word) > m * n or not (cnt := Counter(word)) <= Counter(chain(*board)):
            return False
        if cnt[word[0]] < cnt[word[-1]]:
            word = word[::-1]
        return any(dfs(i, j, 0) for (i, j) in product(range(m), range(n)))
