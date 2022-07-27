class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: 
            return ""
        
        comb = ('0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz')

        def backtrack(idx, partial):
            if idx == len(partial):
                res.append("".join(partial[:]))
                return
            
            for c in comb[int(digits[idx])]:
                partial[idx] = c
                backtrack(idx + 1, partial)
             
                
        res = list()
        partial = ['0' for _ in range(len(digits))]
        backtrack(0, partial)
        return res