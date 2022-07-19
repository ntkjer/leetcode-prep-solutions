class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = list()
        trie = {}
        end = "$"
        
        for word in wordDict:
            node = trie
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node[end] = word
        
        
        
        def backtrack(word, partial):
            root = trie            
            for i, char in enumerate(word):
                if end in root:
                    backtrack(word[i:], partial + [root[end]])
                    
                if char not in root:
                    return
                root = root[char]
                
            if end in root:
                res.append(" ".join(partial + [root[end]]))
                
        
        
        root = trie
        backtrack(s, [])
        return res