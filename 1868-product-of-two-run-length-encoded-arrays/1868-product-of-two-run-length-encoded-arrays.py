class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        
        m, n = len(encoded1), len(encoded2)
        i, j = 0, 0
        res = list()
        v1, v2 = None, None
        f1, f2 = None, None
        
        while i < m or j < n:
            if not f1 and i < m:
                v1, f1 = encoded1[i]
                i += 1
            if not f2 and j < n:
                v2, f2 = encoded2[j]
                j += 1
            
            min_freq = min(f1, f2)
            cur_product = v1 * v2
            if res and res[-1][0] == cur_product:
                res[-1][1] += min_freq
            else:
                res.append([cur_product, min_freq])
            
            f1 -= min_freq
            f2 -= min_freq
            
        return res
            
            