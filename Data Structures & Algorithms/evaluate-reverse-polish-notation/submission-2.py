class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # trong khi tokens vẫn chưa tính ra kết quả 
        while len(tokens) > 1:
            for i in range(len(tokens)):
                # nếu vị trị index là các kí tự tính toán
                # lấy 2 vị trí sau nó là số để tính
                if tokens[i] in "+-*/":
                    a = int(tokens[i-2])
                    b = int(tokens[i-1])
                    if tokens[i] == '+':
                        result = a + b
                    elif tokens[i] == '-':
                        result = a - b
                    elif tokens[i] == '*':
                        result = a * b
                    elif tokens[i] == '/':
                        result = int(a / b)
                    # gộp lại bỏ 2 thằng kí tự 2 đầu, thêm result vào và gộp với
                    # toàn bộ phía sau
                    tokens = tokens[:i-2] + [str(result)] + tokens[i+1:]
                    # thoát ra để chạy lại vòng
                    break
        return int(tokens[0])

