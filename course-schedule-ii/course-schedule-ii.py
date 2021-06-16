class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # return a topological ordering
        
        graph = defaultdict(list)
        res = list() 
        is_possible = True
        WHITE, GREY, BLACK = 0, 1, 2
        
        for relation in prerequisites:
            next_course, prev_course = relation
            graph[prev_course].append(next_course)

        visited = {v: WHITE for v in range(numCourses)}
        
        def dfs(graph, vertex):
            nonlocal is_possible
            visited[vertex] = GREY
            for edge in graph[vertex]:
                if visited[edge] == WHITE:
                    dfs(graph, edge)
                elif visited[edge] == GREY:
                    is_possible = False
            visited[vertex] = BLACK
            res.append(vertex)
        
        for course in range(numCourses):
            if visited[course] is WHITE:
                dfs(graph, course)
        
        return reversed(res) if is_possible else list()
            