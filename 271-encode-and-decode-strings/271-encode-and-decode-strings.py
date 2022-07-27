class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = list()
        delim = "$"
        for w in strs:
            res.append(str(len(w)) + delim + w)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        delim = "$"
        N = len(s)
        i = 0
        j = 0
        res = list()
        while i < N:
            while s[i] != delim:
                i += 1
    
            length = int(s[j: i])
            
            res.append(s[i + 1: length + i + 1])
            i = length + i + 1
            j = i
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))