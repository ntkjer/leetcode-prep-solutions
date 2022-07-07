class Solution:
    def isValid(self, s: str) -> bool:
        closing = {")": "(", "}": "{", "]": "["}
        
        stack = []
        for ch in s:
            if stack and ch in closing:
                if stack[-1] != closing[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        
        print(stack)
        return True if not stack else False