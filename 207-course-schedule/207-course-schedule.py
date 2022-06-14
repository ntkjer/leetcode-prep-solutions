class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        
        for pre,course in prerequisites:
            adj[course].append(pre)
        
        visit = set()
        
        def dfs(course):
            if course in visit:
                return False
            if not adj[course]:
                return True
            visit.add(course)
                
            for nei in adj[course]:
                if not dfs(nei):
                    return False
            adj[course] = []
            visit.remove(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course): return False
        return True
                
        
        