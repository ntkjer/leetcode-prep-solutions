class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        root = self.root
        for ch in word:
            if ch not in root.children:
                root.children[ch] = TrieNode()
            root = root.children[ch]
        root.end = True
        
        
    def search(self, word: str) -> bool:
        def search_node(node, word):
            for idx, ch in enumerate(word):
                if ch not in node.children:
                    if ch == ".":
                        for child_key in node.children:
                            if child_key != node.end and search_node(node.children[child_key], word[idx + 1:]):
                                return True
                    return False
                node = node.children[ch]
            return node.end
        
        return search_node(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)