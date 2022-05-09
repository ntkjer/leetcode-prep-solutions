class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for c in s:
            if c.isalnum():
                chars.append(c.lower())
                
        if len(chars) == 0:
            return True
        
        left, right = 0, len(chars) - 1
        while left <= right:
            if chars[left] == chars[right]:
                left, right = left + 1, right - 1
            else:
                return False
        return True