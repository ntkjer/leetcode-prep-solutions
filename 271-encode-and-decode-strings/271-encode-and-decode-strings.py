class Codec:
    def __init__(self):
        self.delimeter = "$"
        
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = list()
        for word in strs:
            res.append(str(len(word)) + self.delimeter + word)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = list()
        i = 0
        j = 0
        while i < len(s):
            while s[i] != self.delimeter:
                i += 1
            length = int(s[j: i])
            
            res.append(s[i + 1: i + length + 1])
            
            i = length + 1 + i
            j = i
        return res
        
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))