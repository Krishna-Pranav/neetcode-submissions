from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        # flowPac = [[True for _ in range(n)] for _ in range(m)]
        # flowAtl = [[True for _ in range(n)] for _ in range(m)]
        # for i in range(1, m):
        #     for j in range(1, n):
        #         flowPac[i][j] = (flowPac[i-1][j] and heights[i-1][j] <= heights[i][j]) or (flowPac[i][j-1] and heights[i][j-1] <= heights[i][j])
        # for i in range(m-2, -1, -1):
        #     for j in range(n-2, -1, -1):
        #         flowAtl[i][j] = (flowAtl[i+1][j] and heights[i+1][j] <= heights[i][j]) or (flowAtl[i][j+1] and heights[i][j+1] <= heights[i][j])

        # results = []
        # for i in range(m):
        #     for j in range(n):
        #         if flowPac[i][j] and flowAtl[i][j]:
        #             results.append([i, j])
        # return results
        pac, pacSeen = deque(), set()
        atl, atlSeen = deque(), set()
        for i in range(m):
            pac.append((i, 0))
            pacSeen.add((i, 0))
            atl.append((i, n-1))
            atlSeen.add((i, n-1))
        for j in range(1, n):
            pac.append((0, j))
            pacSeen.add((0, j))
        for j in range(n-1):
            atl.append((m-1, j))
            atlSeen.add((m-1, j))

        def bfs(q, seen):
            while q:
                i, j = q.popleft()
                for ni, nj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    r, c = i+ni, j+nj
                    if 0 <= r < m and 0 <= c < n and heights[r][c] >= heights[i][j] and (r, c) not in seen:
                        q.append((r,c))
                        seen.add((r, c))

        bfs(pac, pacSeen)
        bfs(atl, atlSeen)
        return list(pacSeen.intersection(atlSeen))


