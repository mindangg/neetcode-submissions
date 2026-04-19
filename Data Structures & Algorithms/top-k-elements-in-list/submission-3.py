class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = defaultdict(list)
        for num in nums:
            if num not in hash:
                hash[num] = 0
            hash[num] += 1

        arr = []
        for key, value in hash.items():
            arr.append([value, key])
        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res