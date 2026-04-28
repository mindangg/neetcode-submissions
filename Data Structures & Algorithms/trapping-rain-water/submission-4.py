class Solution:
    def trap(self, height: List[int]) -> int:
        # không có height thì trả về 0
        if not height:
            return 0
        n = len(height)
        res = 0

        # chạy vòng for để kiếm từng i
        for i in range(n):
            leftMax = rightMax = height[i]

            # kiếm thanh cao nhất trong cái khoảng của i vì 
            for j in range(i):
                leftMax = max(leftMax, height[j])

            for k in range(i + 1, n):
                rightMax = max(rightMax, height[k])

            res += min(leftMax, rightMax) - height[i]
        return res 


            
