class Solution:
    def isPossible(self, board, row, col):
        for i in range(row):
            if board[i][col] == "Q":
                return False
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1
        i, j = row, col
        while i >= 0 and j < len(board):
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1
        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        # board = [[".", ".", ".", "."], [".", ".", ".", "."], [".", ".", ".", "."], [".", ".", ".", "."]]
        result = []
        def backtrace(idx, qs):
            # print(idx, qs)
            # print(board)
            if idx == n:
                if qs == n:
                    boardCopy = []
                    for i in board:
                        boardCopy.append("".join(i))
                    result.append(boardCopy)
                return
            for i in range(n):
                if self.isPossible(board, idx, i):
                    board[idx][i] = "Q"
                    backtrace(idx+1, qs+1)
                    board[idx][i] = "."
        backtrace(0, 0)
        return result