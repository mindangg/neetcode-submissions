class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1
        # dùng 2 con trỏ
        while l < r:
            res = max(res, min(heights[l], heights[r]) * (r - l))
            # thanh nào ngắn hơn thì dịch con trỏ 2 thanh đó vì muốn kiếm
            # diện tích lớn nhất nên giữ lại cái cao hơn
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res


