class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {i: set() for i in range(numCourses)}
        
        for course, req in prerequisites:
            graph[course].add(req)
        
        visit = {}
        def dfs(course):
            if course in visit:
                return visit[course]
            
            visit[course] = True
            for nei in graph[course]:
                if dfs(nei):
                    return True
                
            visit[course] = False
        
        for course in range(numCourses):
            if dfs(course):
                return False
            
        return True