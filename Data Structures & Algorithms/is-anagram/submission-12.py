class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # nếu độ dài 2 chuỗi khác thì sai
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        # dùng hashmap để đếm số lượng kí tự xuất hiện
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT