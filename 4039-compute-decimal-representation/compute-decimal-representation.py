class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        l=[]
        s=str(n)[::-1]
        for i in range(len(s)):
            if s[i]!="0":
                l.append(int(s[i]+("0"*i)))
        return l[::-1]