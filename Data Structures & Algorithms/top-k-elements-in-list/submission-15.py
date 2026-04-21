class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force
        # tạo 1 hashmap lưu số lần xuất hiện 1 số
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        # tạo 1 array dùng để lưu số và số lần xuất hiện, rồi sắp xếp nó
        arr = []
        for num, count in freq.items():
            arr.append([count, num])
        arr.sort()

        # lấy k phần tử có số lần xuất hiện nhiều nhất
        res = []
        for i in range(k):
            res.append(arr.pop()[1])

        return res


        

