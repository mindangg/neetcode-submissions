class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            check = set()
            for j in range(i, len(s)):
                if s[j] in check:
                    break
                check.add(s[j])
            res = max(res, len(check))
        return res