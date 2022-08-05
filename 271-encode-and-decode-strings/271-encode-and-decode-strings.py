class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # number, delimeter, word
        res = list()
        for word in strs:
            res.append(str(len(word)) + "$" + word)
        return "".join(res)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        j = 0
        n = len(s)
        res = list()
        
        while i < n:
            while s[i] != "$":
                i += 1
            
            length = int(s[j: i])
            
            res.append(s[i + 1: i + length + 1])
        
            i = length + i + 1
            j = i
            
        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))