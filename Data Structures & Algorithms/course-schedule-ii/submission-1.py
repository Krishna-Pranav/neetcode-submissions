class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph= { i: [] for i in range(numCourses)}
        indegree=[0]*numCourses 

        for course,prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course]+=1
        
        q=collections.deque()    
        res=[]    
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                res.append(i)
        
        while q :
            node= q.popleft()
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei] == 0 :
                    q.append(nei)
                    res.append(nei)

        return res if len(res)==numCourses else []