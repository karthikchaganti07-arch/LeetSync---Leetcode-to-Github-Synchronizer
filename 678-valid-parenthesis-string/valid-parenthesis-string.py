class Solution:
    def checkValidString(self, s: str) -> bool:
        l=h=0
        for i in s:
            if i=="(":
                l+=1
                h+=1
            elif i==")":
                h-=1
                l-=1
            else:
                l-=1
                h+=1
            if h<0:
                return bool(0)
            if l<0:
                l=0
        return l==0