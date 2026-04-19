class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26 # create an array (a-z) 26 characters

            for c in s:
                count[ord(c) - ord("a")] += 1 # find the ascii for example a = 80 80 - 80 = 0 or b = 81
                
            res[tuple(count)].append(s)
        return res.values()

        