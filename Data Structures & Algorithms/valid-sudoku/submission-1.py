# class Solution:
#     def checkIsValid(self, k, board, i, j):
#         for a in range(9):
#             if k == board[i][a]:
#                 return False
#             if k == board[a][j]:
#                 return False
#         for a in range(3*(i//3), 3*(i//3)+3):
#             for b in range(3*(j//3), 3*(j//3)+3):
#                 if board[a][b]==k:
#                     return False
#         return True


#     def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for i in range(9):
        #     for j in range (9):
        #         if board[i][j] == ".":
        #             for k in range(1,10):
        #                 if self.checkIsValid(str(k), board, i, j):
        #                     board[i][j] = str(k)
        #                 else:
        #                     continue
        #                 if not self.isValidSudoku(board):
        #                     board[i][j] = "."
        #             if board[i][j] == ".":
        #                 return False
        # print(board)
        # return True

class Solution:
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == ".":
                    continue

                # Calculate box index
                box_id = (i // 3) * 3 + (j // 3)

                # Check duplicates
                if val in rows[i] or val in cols[j] or val in boxes[box_id]:
                    return False

                # Add value
                rows[i].add(val)
                cols[j].add(val)
                boxes[box_id].add(val)

        return True