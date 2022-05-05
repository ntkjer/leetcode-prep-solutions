class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for w in strs:
            res += str(len(w)) + "#" + w
        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        N = len(s)
        while i < N:
            j = i
            while s[j] != "#": #might be 55 or 500
                j += 1
                
            length = int(s[i: j])
            word = s[j + 1: j + 1 + length]
            res.append(word)
            i = j + 1 + length
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))