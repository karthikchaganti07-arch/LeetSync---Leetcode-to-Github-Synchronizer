class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        see = set()
        r = set()
        for i in range(len(s) - 9):
            l= s[i:i+10]
            if l in see:
                r.add(l)
            else:
                see.add(l)
        return list(r)