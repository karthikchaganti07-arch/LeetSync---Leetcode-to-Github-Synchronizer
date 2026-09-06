class Solution:
    def getLucky(self, s: str, k: int) -> int:
        r=""
        for i in s:
            r+=str(ord(i)-ord("a")+1)
        while k!=0:
            c=0
            for i in r:
                c+=int(i)
            r=str(c)
            k-=1
        return int(r)