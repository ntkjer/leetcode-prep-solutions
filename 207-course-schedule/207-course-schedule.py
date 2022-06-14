class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()
        courses = {i: [] for i in range(numCourses)}
        
        for prereq, course in prerequisites:
            if course not in courses:
                courses[course] = []
            courses[course].append(prereq)
        
        
        def dfs(course):
            if course in visit:
                return False
            if not courses[course]:
                return True
            visit.add(course)
            for nei in courses[course]:
                if not dfs(nei):
                    return False
            visit.remove(course)
            courses[course] = []
            return True
        
    
        for course in range(numCourses):
            if not dfs(course): 
                return False
        return True