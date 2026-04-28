class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        res = 0
        l, r = 0, len(height) - 1
        # 2 biến 2 đầu lưu giữ thanh cao nhất ở bên đó
        leftMax, rightMax = height[l], height[r]
        while l < r:
            # 2 thanh 2 đầu ko thể có nước

            # nước ở vị trí i bất kì phụ thuộc vào bên có chiều cao thấp hơn vì
            # nó sẽ tràn ở bên đó

            # nếu bên trái thấp hơn thì dịch con trỏ bên trái vì nước sẽ chỉ có
            # thể bằng bên thấp hơn nên dịch bên phải thì không thay đổi nước
            if leftMax < rightMax:
                l += 1
                # nước bằng thanh ngắn hơn trừ chiều cao vị trí thanh i hiện tại
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            # bên phải y chang nhưng ngược lại
            else:
                r -= 1
                # nước bằng thanh ngắn hơn trừ chiều cao vị trí thanh i hiện tại
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res