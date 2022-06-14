class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        
        for pre,course in prerequisites:
            adj[course].append(pre)
        
        visit = [False] * numCourses
        path = [False] * numCourses
        
        def dfs(course):
            if visit[course]:
                return False
            
            if path[course]:
                return True
            
            visit[course] = True
            path[course] = False
            for nei in adj[course]:
                if not dfs(nei):
                    return False
                
            path[course] = True
            visit[course] = False
            return True
        
        for course in range(numCourses):
            if not dfs(course): return False
            
        return True
                
        
        