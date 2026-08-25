class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                num2 = stack.pop()
                num1 = stack.pop()
                result = num1 + num2
                stack.append(result)
            elif t == '-':
                num2 = stack.pop() 
                num1 = stack.pop()
                result = num1 - num2
                stack.append(result)
            elif t == '*':
                num2 = stack.pop() 
                num1 = stack.pop()
                result = num1 * num2
                stack.append(result)
            elif t == '/':
                num2 = stack.pop() 
                num1 = stack.pop()
                result = int(num1 / num2)
                stack.append(result)
            else:
                stack.append(int(t))
        
        return stack.pop()

