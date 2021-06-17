#class Node(object):
#    def __init__(self):
#        self.indegree = 0
#        self.neighbors = list()

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # approach
        # 1. extract dependency rules from input
        # 2. put dependency rules into a graph 
        #       letters as vertex and dependencies as edges
        # 3. topologically sort the nodes

        adj_list = defaultdict(set)
        in_degree = Counter({c: 0 for word in words for c in word})
        
        result = list()    
        total_edges = 0
        
        for first, second in zip(words, words[1:]):
            if len(second) < len(first) and first.startswith(second):
                return '' # it is a prefix and invalid
            
            for a, b in zip(first, second):
                if a != b:
                    if b not in adj_list[a]:
                        in_degree[b] += 1
                        adj_list[a].add(b)
                    break
                    
        q = collections.deque()         
        for c in in_degree:
            if in_degree[c] == 0:
                q.append(c)

        while q:
            curr = q.popleft()
            result.append(curr)
            for neighbor in adj_list[curr]:
                in_degree[neighbor] -= 1
                
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        if len(result) < len(in_degree):
            return ''
        else:
            return ''.join(result)

            
            
    