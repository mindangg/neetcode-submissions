class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        ok = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (j != i):
                    ok *= nums[j]
            output.append(ok)
            ok = 1
        return output
        