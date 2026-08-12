class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        q = deque()
        seen = set()
        sides = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(m):
            if board[i][0] == 'O':
                q.append((i, 0))
                board[i][0] = 'T'
            if board[i][n-1] == 'O':
                q.append((i, n-1))
                board[i][n-1] = 'T'
        for j in range(n):
            if board[0][j] == 'O':
                q.append((0, j))
                board[0][j] = 'T'
            if board[m-1][j] == 'O':
                q.append((m-1, j))
                board[m-1][j] = 'T'
        
        while q:
            r, c = q.popleft()
            seen.add((r, c))
            for i, j in sides:
                ni, nj = r+i, c+j
                if 0<=ni<m and 0<=nj<n and (ni, nj) not in seen and board[ni][nj] == 'O':
                    board[ni][nj] = 'T'
                    q.append((ni, nj))
                    seen.add((ni, nj))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'T':
                    board[i][j] = 'O'