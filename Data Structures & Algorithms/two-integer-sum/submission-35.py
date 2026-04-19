class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       hashmap = defaultdict(list)
       for i, n in enumerate(nums):
          difference = target - nums[i]
          if difference in hashmap:
            return [hashmap[difference], i]
          hashmap[n] = i
          