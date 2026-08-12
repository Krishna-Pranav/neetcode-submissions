class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        courses = [[] for _ in range(n)]

        for course in prerequisites:
            courses[course[0]].append(course[1])

        seen = set()
        pathSeen = set()

        def dfs(g, idx):
            seen.add(idx)
            pathSeen.add(idx)

            for i in g[idx]:
                if i in pathSeen:
                    return True

                if i not in seen and dfs(g, i):
                    return True

            pathSeen.remove(idx)
            return False

        for i in range(n):
            if i not in seen:
                if dfs(courses, i):
                    return False

        return True