class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src, dst, cost in times:
            graph[src].append((dst, cost))
        
        queue = [(0, k)]
        visited = set()
        max_cost = 0
        
        while queue:
            cost, node = heapq.heappop(queue)
            if node in visited:
                continue
            
            visited.add(node)
            max_cost = max(max_cost, cost)
            
            neighbors = graph[node]
            for nei in neighbors:
                new_node, new_cost = nei
                if new_node not in visited:
                    curr_cost = cost + new_cost
                    heapq.heappush(queue, (curr_cost, new_node))
                    
        return max_cost if len(visited) == n else -1