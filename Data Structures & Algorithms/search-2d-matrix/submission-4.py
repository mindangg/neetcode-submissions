class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            # lấy hàng ở giữa
            row = (top + bot) // 2
            # nếu target lớn hơn hẳn phần tử cuối
            # dịch phần top xuống vì row tăng dần
            if target > matrix[row][-1]:
                top = row + 1
            # nếu target nhỏ hơn hẳn phần tử cuddaafuối
            # dịch phần bot lên vì row tăng dần
            elif target < matrix[row][0]:
                bot = row - 1
            # nếu ko thì row hiện tại có target
            else:
                break

        # nếu top và bot đi qua mà vẫn ko break có nghĩa ko tồn tại target
        if not (top <= bot): return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1

        # tìm binary search trong row đã tìm được
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False



