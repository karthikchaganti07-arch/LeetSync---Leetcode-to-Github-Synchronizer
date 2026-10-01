class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        d={
            ")":"(","}":"{","]":"["
        }
        for i in s:
            if i in d.values():
                l.append(i)
            elif i in d:
                if not l or l[-1]!=d[i]:
                    return bool(0)
                l.pop()
        return not l