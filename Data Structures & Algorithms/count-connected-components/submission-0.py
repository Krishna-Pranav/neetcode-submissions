class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen = set()
        def dfs(idx):
            seen.add(idx)
            for i in graph[idx]:
                if i not in seen:
                    dfs(i)

        components = 0
        for i in range(n):
            if i not in seen:
                components += 1
                dfs(i)
        return components