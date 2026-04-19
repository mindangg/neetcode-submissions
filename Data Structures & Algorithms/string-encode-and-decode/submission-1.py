class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in range (len(strs)):
            s += strs[i]
            s+='é'
        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        og = ''
        for i in range(len(s)):
            if s[i] != 'é':
                og += s[i]
            else:
                strs.append(og)
                og = ''
        return strs
