class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        # 2 mảng để tính số lần xuất hiện của từng chữ cái
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # đếm xem 2 string giống nhau bao nhiu chữ
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            # nếu giống nhau hết 26 kí tự thì đúng có tồn tại permutation
            if matches == 26: return True

            # con trỏ r di chuyển, tại vị trí index đó của s2 sẽ tăng lên 1 xuất hiện
            # check xem có bằng với s1 ko
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            if s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # y chang nhưng sẽ ngược lại với l    
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            if s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26

            
