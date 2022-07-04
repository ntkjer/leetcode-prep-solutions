class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = list()
        
        for word in strs:
            res.append(str(len(word)) + "$" + word)
        
        return ",".join(res)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        j = 0
        N = len(s)
        res = list()
        while i < N:
            while s[i] != "$":
                i += 1
            length = int(s[j: i])
            res.append(s[i + 1: length + i + 1])
            i = length + i + 1
            j = i + 1
            
        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))