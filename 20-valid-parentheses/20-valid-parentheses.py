class Solution:
    def isValid(self, s: str) -> bool:
        
        close = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:       
            if stack and c in close:
                if not stack: return False
                p = stack.pop()

                if close[c] != p:
                    return False
                continue
            stack.append(c)
        print(stack)
        
        return not(stack)