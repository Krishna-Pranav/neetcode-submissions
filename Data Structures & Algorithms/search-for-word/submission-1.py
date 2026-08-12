class Solution:
    def findWord(self, board, ignore, current, word, formed):
        print(word[formed-1])
        if formed == len(word):
            return True
        i, j = current
        m, n = len(board), len(board[0])
        exist = False
        if not exist and i > 0 and (i-1, j) not in ignore and board[i-1][j] == word[formed]:
            ignore.append((i-1, j))
            exist = self.findWord(board, ignore, (i-1, j), word, formed+1)
            ignore.pop()
            # if exist == False:
            #     ignore.pop()

        if not exist and i < m-1 and (i+1, j) not in ignore and board[i+1][j] == word[formed]:
            ignore.append((i+1, j))
            exist = self.findWord(board, ignore, (i+1, j), word, formed+1)
            ignore.pop()

        if not exist and j > 0 and (i, j-1) not in ignore and board[i][j-1] == word[formed]:
            ignore.append((i, j-1))
            exist = self.findWord(board, ignore, (i, j-1), word, formed+1)
            ignore.pop()

        if not exist and j < n-1 and (i, j+1) not in ignore and board[i][j+1] == word[formed]:
            ignore.append((i, j+1))
            exist = self.findWord(board, ignore, (i, j+1), word, formed+1)
            ignore.pop()

        return exist

    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    exist = self.findWord(board, [(i, j)], (i, j), word, 1)
                    if exist:
                        return exist
        return False