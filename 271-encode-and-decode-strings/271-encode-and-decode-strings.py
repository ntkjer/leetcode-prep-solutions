class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = list()
        delimeter = "$"
        
        for word in strs:
            curr = str(len(word)) + delimeter + word
            res.append(curr)
            
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        delimeter = "$"
        i = 0
        j = 0
        res = list()
        while i < len(s):
            j = i + 1
            while s[j] != delimeter:
                j += 1
                
            length = int(s[i: j])
            
            res.append(s[j + 1: j + length + 1])
            
            i = length + j + 1
            
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))