class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        res = [0] * k
        active = {}
        for uid, t in logs:
            active[uid] = active.get(uid, []) + [t]
        
        for uid in active:
            total_activity = len(set(active[uid]))
            res[total_activity - 1] += 1
            
        return res