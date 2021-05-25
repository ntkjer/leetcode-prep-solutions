class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        @lru_cache(maxsize=None) 
        def recur(i, j) -> int:
            if i == len(s1) or j == len(s2):
                return 0
            if s1[i] == s2[j]:
                return ord(s1[i]) + recur(i + 1, j + 1)
            else:
                return max(recur(i + 1, j), recur(i, j + 1))

        total_sum = sum(map(ord, (s1 + s2)))
        #for c1, c2 in zip(s1, s2):
        #    total_sum += ord(c1) + ord(c2)
        res = recur(0,0) 
        recur.cache_clear()
        return total_sum - 2*res
            