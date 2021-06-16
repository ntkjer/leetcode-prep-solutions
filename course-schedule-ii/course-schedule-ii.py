class Node(object):
    '''
    We need both:
        in_degree of a node 
        all its outward edges to utilize Kahn's Algorithm.
    '''
    def __init__(self):
        self.in_degree = 0
        self.out_nodes = list()

        
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        Kahn's Algorithm
        ''' 
        from collections import defaultdict, deque

        total_edges = 0
        edges_removed = 0
        topological_order = list() 
        
        graph = defaultdict(Node)

        for relation in prerequisites:
            next_course, prev_course = relation
            graph[next_course].in_degree += 1
            graph[prev_course].out_nodes.append(next_course)
            total_edges += 1

        edgeless = deque()

        for course in range(numCourses):
            if graph[course].in_degree == 0:
                edgeless.append(course)
         
        while edgeless:
            curr = edgeless.popleft()
            topological_order.append(curr)    
            for child in graph[curr].out_nodes:
                graph[child].in_degree -= 1

                if graph[child].in_degree == 0:
                    edgeless.append(child)

            edges_removed += 1
                    
        return list() if len(topological_order) != numCourses else topological_order
    
        
    def findOrder_DFS(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        Time: 96 ms (83.72%), Space: 17.6 MB (18.35%) - LeetHub
        '''
        
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
            if not is_possible:
                return 
            
            for edge in graph[vertex]:
                if visited[edge] == WHITE:
                    dfs(graph, edge)
                elif visited[edge] == GREY:
                    is_possible = False

            visited[vertex] = BLACK
            res.append(vertex)
        
        for course in range(numCourses):
            if visited[course] == WHITE:
                dfs(graph, course)
        
        return reversed(res) if is_possible else list()
            