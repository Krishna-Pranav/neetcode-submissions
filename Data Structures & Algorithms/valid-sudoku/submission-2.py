class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:        
        def isValid(val, i, j):
            for r in range(9):
                if r!=i and board[r][j] == val:
                    return False
                if r!=j and board[i][r] == val:
                    return False
            row, col = 3*(i//3), 3*(j//3)
            for r in range(row, row+3):
                for c in range(col, col+3):
                    if r!=i and c!=j and board[r][c]==val:
                        return False
            return True
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if not isValid(board[i][j], i, j):
                        return False

        return True