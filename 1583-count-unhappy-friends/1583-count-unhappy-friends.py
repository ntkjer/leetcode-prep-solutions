class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        seen = {}
        for pair in pairs:
            seen[pair[0]] = pair[1]
            seen[pair[1]] = pair[0]
        
        ranked_preferences = {}
        for i in range(len(preferences)):
            for preference in preferences[i]:
                if preference == seen[i]:
                    break
                if i not in ranked_preferences:
                    ranked_preferences[i] = set()
                    
                ranked_preferences[i].add(preference)
                
        res = 0
        for person, preferences in ranked_preferences.items():
            for friend in preferences:
                if friend in ranked_preferences and person in ranked_preferences[friend]:
                    res += 1
                    break
        
        
        return res