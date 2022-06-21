class TrieNode:
    def __init__(self, key=""):
        self.key = key
        self.children = {}
        self.end = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        root = self.root
        for ch in word:
            if ch not in root.children:
                root.children[ch] = TrieNode(ch)
            root = root.children[ch]
        root.end = True

    def search(self, word: str) -> bool:
        def searchNode(node, word):
            for i, ch in enumerate(word):
                if ch not in node.children:
                    if ch == ".":
                        for child in node.children:
                            if child != node.end and searchNode(node.children[child], word[i + 1:]):
                                return True
                    return False
                node = node.children[ch]
                 
            return node.end
        
        return searchNode(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)