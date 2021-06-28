class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        self.end = "$"
        
    def addWord(self, word: str) -> None:
        node = self.trie
        
        for char in word:
            if not char in node:
                node[char] = {}
            node = node[char]
        node[self.end] = True

    def search(self, word: str) -> bool:
        
        def search_in_node(word, node):
            for i, ch in enumerate(word):
                if ch not in node:
                    if ch == ".":
                        for x in node:
                            if x != self.end and search_in_node(word[i + 1:], node[x]):
                                return True
                    return False
                node = node[ch]
            return self.end in node

        return search_in_node(word, self.trie)
                    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)