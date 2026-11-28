class Solution:
    def makeFancyString(self, s: str) -> str:
        r=[]
        for i in s:
            if len(r)<2 or r[-1]!=i or r[-2]!=i:
                r.append(i)
        return "".join(r)