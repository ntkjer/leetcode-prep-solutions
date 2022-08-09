class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        ops = set(["+", "-", "/", "*"])
        
        # 10, 6, 9, 3
        # 10, 6, 9, 12
        # 10, 6, 9, 12, -11
        # 10, 6, 9, -132 / 9
        
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
                continue
   
            y = stack.pop()
            x = stack.pop()

            if token == "*":
                stack.append(x * y)
            elif token == "+":
                stack.append(x + y)
            elif token == "/":
                stack.append(int(x / y))
            elif token == "-":
                stack.append(x - y)
                    
        print(stack)           
        return stack.pop()