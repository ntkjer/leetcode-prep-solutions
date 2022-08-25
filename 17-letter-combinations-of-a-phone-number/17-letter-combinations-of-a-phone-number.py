class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = list()
        if not digits: return res
        combinations = {"0": [], "1": [], "2": ["a", "b", "c"], "3": ["d", "e", "f"], 
                        "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], 
                        "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        
        
        def backtrack(idx=0, partial=[]):
            if idx == len(digits):
                res.append("".join(partial[:]))    
                
            if idx >= len(digits): 
                return
            
            for comb in combinations[digits[idx]]:
                partial.append(comb)
                backtrack(idx + 1, partial)
                partial.pop()
        
        backtrack()
        return res