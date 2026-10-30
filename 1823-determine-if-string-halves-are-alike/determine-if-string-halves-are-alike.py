class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s)//2
        a=s[:n]
        b=s[n:]
        c=d=0
        l=["a","e","i","o","u"]
        for i in a:
            if i.lower() in l:
                c+=1
        for i in b:
            if i.lower() in l:
                d+=1
        return c==d