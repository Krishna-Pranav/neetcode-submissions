class Solution:
    def bfs(self, grid, island):
        while island:
            i, j = island.popleft()
            grid[i][j] = "c"
            if i > 0 and grid[i-1][j] == "1" and (i-1, j) not in island:
                island.append((i-1, j))
            if j > 0 and grid[i][j-1] == "1" and (i, j-1) not in island:
                island.append((i, j-1))
            if i < len(grid)-1 and grid[i+1][j] == "1" and (i+1, j) not in island:
                island.append((i+1, j))
            if j < len(grid[0])-1 and grid[i][j+1] == "1" and (i, j+1) not in island:
                island.append((i, j+1))

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    island = deque()
                    island.append((i, j))
                    self.bfs(grid, island)
        return count