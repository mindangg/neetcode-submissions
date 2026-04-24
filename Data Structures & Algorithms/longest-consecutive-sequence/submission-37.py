class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        longest = 0

        for num in check:
            if num - 1 not in check:
                length = 0
                while num + length in check:
                    length += 1
                longest = max(longest, length)
        return longest