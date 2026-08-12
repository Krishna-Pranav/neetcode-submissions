class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        fresh = []
        time = -1
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh.append((i, j))
                elif grid[i][j] == 2:
                    rotten.append((i, j))
        while rotten:
            time += 1
            for _ in range(len(rotten)):
                i, j = rotten.popleft()
                sides = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for di, dj in sides:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < m and 0 <= nj < n and (ni, nj) in fresh:
                        rotten.append((ni, nj))
                        fresh.remove((ni, nj))
        if fresh:
            return -1
        return max(0, time)
