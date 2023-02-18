'''
48. Rotate Image
https://leetcode.com/problems/rotate-image/
'''


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def helper(matrix, k):
            n = len(matrix)
            submatrix_len = n - 2 * k
            if submatrix_len <= 1:
                return
            start = k
            end = n-k-1
            for i in range(submatrix_len-1):
                buf1, buf2, buf3, buf4 = matrix[start][start+i], matrix[start+i][end], matrix[end][end-i], matrix[end-i][start]
                matrix[start+i][end] = buf1
                matrix[end][end-i] = buf2
                matrix[end-i][start] = buf3
                matrix[start][start+i] = buf4
            helper(matrix, k+1)
        helper(matrix, 0)
