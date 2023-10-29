"""Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place."""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        rows=set()
        cols =set()
        for i in range(m):
            for j in range(n):
                 if matrix[i][j] == 0:
                          rows.add(i)
                          cols.add(j)
        for row in rows:
             for j in range(n):
                      matrix[row][j] = 0

        for col in cols:
                for i in range(m):
                      matrix[i][col] = 0
sl=Solution()
sl.setZeroes
