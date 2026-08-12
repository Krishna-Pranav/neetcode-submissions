class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        courses = [[] for _ in range(n)]
        for course in prerequisites:
            courses[course[0]].append(course[1])
        
        exploring, canbecompleted = set(), set()

        def dfs(course):
            if course in exploring:
                return False
            if course in canbecompleted:
                return True
            
            exploring.add(course)
            for prerequisite in courses[course]:
                if not dfs(prerequisite):
                    return False
            
            exploring.remove(course)
            canbecompleted.add(course)

            return True

        for course in range(n):
            if not dfs(course):
                return False
        return True