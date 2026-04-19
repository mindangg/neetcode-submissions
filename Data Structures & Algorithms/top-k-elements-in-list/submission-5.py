class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = defaultdict(list)
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            if num not in hash:
                hash[num] = 0
            hash[num] += 1
        for key, value in hash.items(): # add value base on freq as key, bucket sort
            freq[value].append(key)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res