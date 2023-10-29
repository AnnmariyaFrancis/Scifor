"""Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal."""
class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat)
        mid = n // 2
        summation = 0
        for i in range(n):
            summation += mat[i][i]
            summation += mat[n-1-i][i]
        if n % 2 == 1:
            summation -= mat[mid][mid]
        return summation
sl=Solution()
sl.diagonalSum