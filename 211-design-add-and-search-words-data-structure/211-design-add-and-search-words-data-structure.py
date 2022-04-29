
class TrieNode:
    
    def __init__(self, data=""):
        self.children = {}
        self.key = data
        self.end = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end = True
        
    def search(self, word: str) -> bool:
        def searchNode(word, node):
            for i,ch in enumerate(word):
                if ch not in node.children:
                    if ch == ".":
                        for x in node.children:
                            if x != node.end and searchNode(word[i + 1:], node.children[x]):
                                return True
                    return False
                node = node.children[ch]
            return node.end
        
        return searchNode(word, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)