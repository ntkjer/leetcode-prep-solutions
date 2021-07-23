class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        string = [] 
        for c in s:
            if c.isalnum():
                string.append(c)
                
        if string == string[::-1]:
            return True
        else:
            return False