class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        c=0
        n=len(mat)
        for i in range(n):
            c+=mat[i][i]
            c+=mat[i][n-1-i]
        if n % 2 == 1:
            c-= mat[n // 2][n // 2]
        return c