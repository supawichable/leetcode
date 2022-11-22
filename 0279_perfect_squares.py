'''
279. Perfect Squares
https://leetcode.com/problems/perfect-squares/
'''


# DP
class Solution1:
    def numSquares(self, n: int) -> int:
    mem = dict()
    squares = [i ** 2 for i in range(0, int(n**0.5) + 1)]
    len_squares = len(squares)
    def dp(x):
        if x in mem:
            return mem[x]
        if x <= 0:
            return 0
        i = 1
        curr = x
        while i < len_squares and squares[i] <= x:
            curr = min(curr, 1 + dp(x - squares[i]))
            i += 1
        mem[x] = curr
        return curr
    return dp(n)

# BFS
class Solution2:
    def numSquares(self, n: int) -> int:
    queue = [n]
    squares = [i**2 for i in range(0, int(n**0.5) + 1)]
    lvl = 0
    while queue:
        new_queue = []
        lvl += 1
        for x in queue:
            for sq in squares:
                if x == sq:
                    return lvl
                elif x < sq:
                    break
                else:
                    new_queue.append(x - sq)
        queue = new_queue

# Four squares and three squares theorem
class Solution3:
    def numSquares(self, n: int) -> int:
        while n % 4 == 0:
            n //= 4
        if n % 8 == 7:
            return 4

        def is_square(x):
            return x == int(x ** 0.5) ** 2
        
        if is_square(n):
            return 1
        i = 1
        sq = i ** 2
        while sq <= n:
            if is_square(n - sq):
                return 2
            i += 1
            sq = i ** 2
        return 3
