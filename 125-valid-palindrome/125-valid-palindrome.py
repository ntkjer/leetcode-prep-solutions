class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for char in s:
            if char.isalnum():
                chars.append(char.lower())
                
        if len(chars) == 0:
            return True
        
        left = 0 
        right = len(chars) - 1
        while left < right:
            if chars[left] == chars[right]: 
                left, right = left + 1, right - 1
            else:
                return False     
        return True