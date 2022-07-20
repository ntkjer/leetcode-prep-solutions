class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                substring = ""
                while stack and stack[-1] != "[":
                    substring = stack.pop() + substring
                stack.pop()
                
                freq = ""
                while stack and stack[-1].isdigit():
                    freq = stack.pop() + freq
                
                stack.append(int(freq) * substring)
                
        return "".join(stack)