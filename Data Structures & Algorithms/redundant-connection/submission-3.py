class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        parent = [i for i in range(n)]
        size = [1] * n

        def find(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(u, v):
            rootu, rootv = find(u), find(v)
            if rootu == rootv:
                return False
            if size[rootu] > size[rootv]:
                parent[rootv] = rootu
                size[rootu] += size[rootv]
            else:
                parent[rootu] = rootv
                size[rootv] += size[rootu]
            return True

        for u, v in edges:
            if not union(u,v):
                return [u,v]