class Solution:
    def encode(self, s: str) -> str:
        # Do not encode it
        # Or encode it to one string if possible
        # Or, split it into two, encode the two substring to their shortest possible length, and combine them

        @lru_cache(maxsize=None)
        def solve(s):
            i = (s + s).find(s, 1)
            if i < len(s):
                encoded = str(len(s) // i) + '[' + solve(s[:i]) + ']' 
            else:
                encoded = s
            
            split_encoded = [solve(s[:i]) + solve(s[i:]) for i in range(1, len(s))]
            return min(split_encoded+[encoded],key=len)


        return solve(s) 
        
            
            
            
            