class Solution:
    def freqAlphabets(self, s: str) -> str:
        res=""
        skip = 0
        for i in range(len(s)):
            if skip > 0:
                skip -= 1
                continue
            if i + 2 < len(s) and s[i+2] == "#":
                r = s[i:i+2]
                res += chr(int(r) + 96)
                skip = 2
            else:
                r = s[i]
                res += chr(int(r) + 96)      
        return res