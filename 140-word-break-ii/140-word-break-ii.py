class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = {}
        end = "$"
        
        for word in wordDict:
            root = trie
            for ch in word:
                if ch not in root:
                    root[ch] = {}
                root = root[ch]
            root[end] = word
        
        
        res = list()
        def backtrack(word="", partial=[]):
            root = trie
            for i, ch in enumerate(word):
                if end in root:
                    partial.append(root[end])
                    backtrack(word[i:], partial)
                    partial.pop()
                    
                if ch not in root:
                    return
                
                root = root[ch]
                
            if end in root:
                partial.append(root[end])
                res.append(" ".join(partial))
                partial.pop()
                
        root = trie
        backtrack(s, [])
        print(res)
        return res
                
        
        