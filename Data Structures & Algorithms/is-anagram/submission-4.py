class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted1 = sorted(s)
        sorted2 = sorted(t)
        if sorted1 == sorted2:
            return True
        return False