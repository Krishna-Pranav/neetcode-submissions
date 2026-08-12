class Solution:
    def sizeOfIsland(self, grid, row, col):
        path = deque()
        path.append((row, col))
        count, m, n = 0, len(grid), len(grid[0])
        while path:
            r, c = path.popleft()
            grid[r][c] = -1
            count += 1
            if r > 0 and (r-1, c) not in path and grid[r-1][c] == 1:
                grid[r-1][c] = -1
                path.append((r-1, c))
            if c > 0 and (r, c-1) not in path and grid[r][c-1] == 1:
                grid[r][c-1] = -1
                path.append((r, c-1))
            if r < m-1 and (r+1, c) not in path and grid[r+1][c] == 1:
                grid[r+1][c] = -1
                path.append((r+1, c))
            if c < n-1 and (r, c+1) not in path and grid[r][c+1] == 1:
                grid[r][c+1] = -1
                path.append((r, c+1))
        return count

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, self.sizeOfIsland(grid, i, j))
        return maxArea