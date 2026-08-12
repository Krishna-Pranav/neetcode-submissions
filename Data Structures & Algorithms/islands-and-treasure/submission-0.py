class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        def bfs(i, j):
            q = deque()
            q.append((i, j))
            seen = [(i, j)]
            count = 0
            while q:
                for _ in range(len(q)):
                    x, y = q.popleft()
                    if grid[x][y] == 0:
                        return count
                    sides = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    for dx, dy in sides:
                        if 0 <= x+dx < m and 0 <= y+dy < n and (x+dx, y+dy) not in seen and grid[x+dx][y+dy] != -1:
                            q.append((x+dx, y+dy))
                            seen.append((x+dx, y+dy))
                count += 1
            return False

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2147483647:
                    temp = bfs(i, j)
                    if temp:
                        grid[i][j] = temp


