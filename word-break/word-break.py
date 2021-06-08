class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # The naive approach to solve this problem is to use recursion and backtracking. 
        # we check every possible prefix of that string in the dictionary of words
            #if it is found in the dictionary, then the recursive function is called for the remaining portion of that string.
            # if in some function call it is found that the complete string is in dictionary, then it will return true.

        words = set(wordDict) 
        @cache 
        def backtrack(s, start):
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in words and backtrack(s, end):
                    return True
            return False
            
        res = backtrack(s, 0)
        return res
            
            
            
       
            
            