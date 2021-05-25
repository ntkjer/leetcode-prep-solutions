class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        memo = {}
        
        def dfs(word):
            if word in memo:
                return memo[word]
            max_longest = 1
            for i in range(len(word)):
                new_word = word[:i] + word[i + 1:]
                if new_word in words:
                    max_longest = max(max_longest, 1 + dfs(new_word))
                    
            memo[word] = max_longest
            return max_longest

        return max(dfs(word) for word in set(words))
            