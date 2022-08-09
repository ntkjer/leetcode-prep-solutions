class Solution:
    def decodeString(self, s: str) -> str:
        
        
        # 3 [ a 2 [ c
        # 3 [ a c c 
        # accaccacc
        stack = []
        for c in s:
            if c == "]":
                tmp = ""
                while stack and stack[-1].isalpha():
                    tmp = stack.pop() + tmp
                
                stack.pop()
                freq = ""
                while stack and stack[-1].isdigit():
                    freq = stack.pop() + freq
                
                stack.append(int(freq) * tmp)
                
                    
            else:
                stack.append(c)
                
        return "".join(stack)