class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        for i in range(len(tokens)):
            if tokens[i] not in "+-*/":
                result.append(tokens[i])
            else:
                b = int(result.pop())
                a = int(result.pop())
                if tokens[i] == '+':
                    result.append(a + b)
                elif tokens[i] == '-':
                    result.append(a - b)
                elif tokens[i] == '*':
                    result.append(a * b)
                elif tokens[i] == '/':
                    result.append(int(a / b))
        return int(result[0])