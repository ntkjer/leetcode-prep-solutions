class Solution:
    def decodeString(self, s: str) -> str:
        # 3 [ a 
        # when a ] is encountered, evaluate the expression
        # and push that eval'ed expr back onto the top of stack.
        
        stack = []
        
        for c in s:
            if c == "]" and stack:
                ch = ""
                while stack and stack[-1] != "[":
                    ch = stack.pop() + ch
                    
                stack.pop() # remove "["
                freq = ""
                while stack and stack[-1].isdigit():
                    freq = stack.pop() + freq
                
                stack.append(ch * int(freq))
                
            else:
                stack.append(c)
        
        return "".join(stack)