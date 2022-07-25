class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "]":
                substring = ""
                while stack and stack[-1] != "[":
                    substring = stack.pop() + substring
                stack.pop()
                freq = ""
                while stack and stack[-1].isdigit():
                    freq = stack.pop() + freq
                stack.append(int(freq) * substring)
                
            else:
                stack.append(c)
                
        return "".join(stack)