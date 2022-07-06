class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        uam = defaultdict(set)
        res = [0] * k
        
        for userID, time in logs:
            uam[userID].add(time)
        
        for user in uam.keys():
            if len(uam[user]) > 0:
                res[len(uam[user]) - 1] += 1
                
        return res