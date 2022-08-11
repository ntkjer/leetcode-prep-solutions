class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        
        res = [] # num, freq
        f1, f2 = 0, 0
        v1, v2 = 0, 0
        i, j = 0, 0
        
        m, n = len(encoded1), len(encoded2)
        
        while i < m and j < n:
            if not f1 and i < m:
                v1, f1 = encoded1[i]
            if not f2 and j < n:
                v2, f2 = encoded2[j]
                
            cur_min = min(f1, f2)
            product = v1 * v2
            
            if res and res[-1][0] == product:
                res[-1][1] += cur_min
            else:
                res.append([product, cur_min])
            
            f1 -= cur_min
            f2 -= cur_min
            
            if not f1:
                i += 1
            if not f2:
                j += 1
        return res 