class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # tạo 1 array với position và speed và 2 phần tử đôi
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []
        for p, s in sorted(pair)[::-1]: # Sort ngược chiều
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]: 
                stack.pop()
        return len(stack)
