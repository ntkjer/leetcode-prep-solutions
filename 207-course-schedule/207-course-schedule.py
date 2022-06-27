class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list = {i: set() for i in range(numCourses)}
        
        for course, pre in prerequisites:
            adj_list[course].add(pre)
            
        
        visit = {}
        def dfs(course):
            if course in visit:
                return visit[course]
            visit[course] = True
            for nei in adj_list[course]:
                if dfs(nei):
                    return True
            visit[course] = False
        
        for course in range(numCourses):
            if dfs(course):
                return False
        return True
        