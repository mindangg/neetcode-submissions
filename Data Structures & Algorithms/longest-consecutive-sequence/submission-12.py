class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        unique_nums = list(dict.fromkeys(nums))
        sortedNums = sorted(unique_nums)
        max_count = 1
        current_count = 1
        for i in range(len(sortedNums) - 1):
            if sortedNums[i + 1] - sortedNums[i] == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 1
        return max_count
