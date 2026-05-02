class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # vì đó là khi array đã sort nên số ở l là min
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[l] <= nums[m]:
                l = m + 1
            else :
                r = m - 1
        return res

            
