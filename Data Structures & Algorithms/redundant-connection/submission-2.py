class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}

        def cycle(edge):
            u, v = edge
            q = deque([u])
            visited = {u}
            while q:
                temp = q.popleft()
                if temp not in graph:
                    continue
                for nei in graph[temp]:
                    if nei == v:
                        return True
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            return False

        for edge in edges:
            if not cycle(edge):
                u, v = edge
                if u in graph:
                    graph[u].append(v)
                else:
                    graph[u] = [v]
                if v in graph:
                    graph[v].append(u)
                else:
                    graph[v] = [u]
            else:
                return edge