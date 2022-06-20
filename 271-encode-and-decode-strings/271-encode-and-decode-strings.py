class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # delimeter = $
        # $4m$3
        #  mmmm   
        res = list()
        for word in strs:
            curr = str(len(word)) + "$" + word
            res.append(curr)
        return "".join(res)
            
            

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = list()
        i = 0
        while i < len(s):
    
            j = i
            while s[j] != "$":
                j += 1
                
            length = int(s[i: j])
            
            res.append(s[j + 1: j + length + 1])
            
            i = length + j + 1
            
        return res
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))