class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            # tạo 1 array 26 kí tự để đếm số lần xuất hiện từng từ
            count = [0] * 26
            for c in s:
                # ord là tính vị trí ascii ví dụ 'a' là 80 'b' là 81 thì trừ đi
                # ta sẽ biết được vị trí của kí tự đó để đặt trong array
                count[ord(c) - ord('a')] += 1
            # gán chữ có số kí tự bằng với nhau vào 1 phần với count là key chữ là value
            res[tuple(count)].append(s)
        return list(res.values())