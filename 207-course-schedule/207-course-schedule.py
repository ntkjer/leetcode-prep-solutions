class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list = {i: set() for i in range(numCourses)}
        
        for course, pre in prerequisites:
            adj_list[course].add(pre)
            
        visit = {}
        def has_cycle(course):
            if course in visit:
                return visit[course]
            visit[course] = True
            for pre in adj_list[course]:
                if has_cycle(pre): 
                    return True
            visit[course] = False
            
        
        for i in range(numCourses):
            if has_cycle(i): 
                return False
        
        return True