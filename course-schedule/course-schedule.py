class GNode(object):
    def __init__(self):
        self.in_degrees = 0
        self.out_nodes = []

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        Kahn's algorithm
        '''
        from collections import defaultdict, deque
        graph = defaultdict(GNode)
        total_deps = 0
        for relation in prerequisites:
            next_course, prev_course = relation
            graph[prev_course].out_nodes.append(next_course)
            graph[next_course].in_degrees += 1
            total_deps += 1
        
        # start from courses with no prereqs
        # can use a set, stack, or queue
        no_dep_courses = deque()
        for index, node in graph.items():
            if node.in_degrees == 0:
                no_dep_courses.append(index)
        
        removed_edges = 0
        while no_dep_courses:
            course = no_dep_courses.pop()
            
            for next_course in graph[course].out_nodes:
                graph[next_course].in_degrees -= 1
                removed_edges += 1
                # while removing edges we may discover new courses
                # that do not have a prereq
                if graph[next_course].in_degrees == 0:
                    no_dep_courses.append(next_course)

        if removed_edges == total_deps:
            return True
        else:
            # if we are here then there is a deadlock and g is not DAG
            return False
        
        
        
    def canFinish_1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        path = [False] * numCourses
        checked = [False] * numCourses
        
        def is_cyclic(course, graph):
            if checked[course]:
                return False
            
            if path[course]:
                return True

            path[course] = True
            res = False
            for child in graph[course]:
                res = is_cyclic(child, graph)
                if res:
                    break
            path[course] = False
            checked[course] = True
            return res
        
        graph = defaultdict(list)
        for relation in prerequisites:
            prev_course, next_course = relation
            graph[prev_course].append(next_course)


        for currCourse in range(numCourses):
            if is_cyclic(currCourse, graph):
                return False
            
        return True
         