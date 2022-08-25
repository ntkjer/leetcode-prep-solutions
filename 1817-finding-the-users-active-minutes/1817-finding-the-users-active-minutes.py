class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        res = [0] * k
        active = collections.defaultdict(set)
        
        for uid, t in logs:
            active[uid].add(t)
        
        for uid in active:
            total = len(active[uid])
            res[total - 1] += 1
        
        return res