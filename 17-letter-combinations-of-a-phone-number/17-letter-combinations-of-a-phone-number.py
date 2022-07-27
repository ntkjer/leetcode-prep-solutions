class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        #combinations = ("0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz")
        res = list()
        comb = {'0': '0', '1': '1', '2': 'abc', '3':'def', 
                '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', 
                '8': 'tuv', '9': 'wxyz'}

        def backtrack(i, partial):
            if i == len(partial):
                res.append("".join(partial[:]))
                return
            
            for c in comb[digits[i]]:
                partial[i] = c
                backtrack(i + 1, partial)
                

            
            
        partial = ["0" for _ in range(len(digits))]
        backtrack(0, partial)
        return res