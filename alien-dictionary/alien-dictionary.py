class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        adj_list = defaultdict(set)
        indegree = Counter({c: 0 for word in words for c in word})
         
        for first, second in zip(words, words[1:]):
            if len(second) < len(first) and first.startswith(second):
                return ''
            
            for a, b in zip(first, second):
                if a != b:
                    if b not in adj_list[a]:
                        adj_list[a].add(b)
                        indegree[b] += 1
                        
                    break
        q = deque()
        
        for char in indegree:
            if indegree[char] == 0:
                q.append(char)
                
        result = list() 
        
        while q:
            curr_course = q.popleft()    
            result.append(curr_course)     
            
            for neighbor in adj_list[curr_course]:
                indegree[neighbor] -= 1
                
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        if len(result) < len(indegree):
            return ''
        else:
            return ''.join(result)
        
                    
            