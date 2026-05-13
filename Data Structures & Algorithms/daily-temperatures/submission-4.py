class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        # tạo 1 stack giữ temp và index
        stack = []

        for i, t in enumerate(temperatures):
            # nếu như stack có phần tử và temp hiện tại lớn hơn phần tử cuối
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                # tính toán số ngày cách để có nhiệt độ lớn hơn qua việc
                # so sánh 2 index
                result[stackI] = i - stackI
            stack.append([t, i])
        return result
