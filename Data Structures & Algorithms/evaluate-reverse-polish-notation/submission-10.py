class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for c in tokens:
            if c == '+':
                res.append(res.pop() + res.pop())
            elif c == '-':
                a, b = res.pop(), res.pop()
                res.append(b - a)
            elif c == '*':
                res.append(res.pop() * res.pop())
            elif c == '/':
                a, b = res.pop(), res.pop()
                res.append(int(float(b) / a))
            else:
                res.append(int(c))
        return res[0]