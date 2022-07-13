class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set(["+", "-", "/", "*"])
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
                continue
            y = stack.pop()
            x = stack.pop()
            if token == "/":
                stack.append(int(x / y))
            elif token == "*":
                stack.append(x * y)
            elif token == "-":
                stack.append(x - y)
            else:
                stack.append(x + y)
                
        return stack.pop()