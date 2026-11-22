class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        n = r*c-1
        l = 0
        while l <= n:
            m = l + (n-l)//2
            mr, mc = m//c, m%c
            if matrix[mr][mc] == target:
                return True
            elif matrix[mr][mc] > target:
                n = m-1
            else:
                l = m+1
        return False