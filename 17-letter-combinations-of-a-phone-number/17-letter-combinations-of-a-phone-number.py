class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return ""
        
        combos = {"0": set(), "1": set(), "2": set(["a", "b", "c"]), "3": set(["d", "e", "f"]),
                 "4": set(["g", "h", "i"]), "5": set(["j", "k", "l"]), "6": set(["m", "n", "o"]),
                 "7": set(["p", "q", "r", "s"]), "8": set(["t", "u", "v"]), "9": set(["w", "x", "y", "z"])}
        
        def backtrack(start=0, partial=[]):
            if start == len(digits):
                res.append("".join(partial[:]))
            if start >= len(digits):
                return
            
            for letter in combos[digits[start]]:
                partial.append(letter)
                backtrack(start + 1)
                partial.pop()
                
        res = list()
        backtrack()
        return res