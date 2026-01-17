class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if x.isdigit() or (x.startswith("-") and x[1:].isdigit()):
                stack.append(int(x))
            else:
                num2, num1 = stack.pop(), stack.pop()
                if x == "+":
                    stack.append(num1 + num2)
                elif x == "-":
                    stack.append(num1 - num2)
                elif x == "*":
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2))
        return stack[0]

