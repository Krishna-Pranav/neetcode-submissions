class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = set()

        def dfs(curr, par):
            seen.add(curr)

            for nei in graph[curr]:
                if nei != par:
                    if nei in seen:
                        return False
                    if not dfs(nei, curr):
                        return False

            return True

        if not dfs(0, -1):
            return False

        return len(seen) == n