class Solution:
    def decodeString(self, s: str) -> str:
        # perhaps a stack?
        # aaa2[b
        
        # tmp = bc
        # tmp = bcbc
        # aaabcbc
        
        stack = []
        for c in s:
            if c == "]": # eval
                tmp = ""
                while stack and stack[-1] != "[":
                    tmp = stack.pop() + tmp
                stack.pop() # remove "["
                
                freq = ""
                while stack and stack[-1].isdigit():
                    freq = stack.pop() + freq
                
                tmp = int(freq) * tmp
                stack.append(tmp)
            else:
                stack.append(c)
                
        return "".join(stack)