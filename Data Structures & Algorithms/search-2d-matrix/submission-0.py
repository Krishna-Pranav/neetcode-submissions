class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        st, fin = 0, m*n-1
        while st <= fin:
            mid = (fin+st)//2
            row, col = mid//n, mid%n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                fin = mid-1
            else:
                st = mid+1
        return False