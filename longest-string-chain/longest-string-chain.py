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
                    cur_len = 1 + dfs(new_word)
                    max_longest = max(max_longest, cur_len)

            memo[word] = max_longest
            return max_longest

        words = set(words)
        return max(dfs(word) for word in words)
            