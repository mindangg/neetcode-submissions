class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # optimal with bucket sort
        # tạo hashmap đến số phần tử xuất hiện        
        count = defaultdict(int)
        # tạo arr bucket với key là số lần xuất hiện từ 0 đến độ dài là độ dài nums
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] += 1

        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for i, n in enumerate(freq[i]):
                res.append(n)
            if len(res) == k:
                return res
        return []

        