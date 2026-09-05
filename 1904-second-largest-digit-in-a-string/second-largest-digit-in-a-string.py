class Solution:
    def secondHighest(self, s: str) -> int:
        l=[]
        for i in s:
            if i.isdigit():
                if int(i) not in l:
                    l.append(int(i))
        l.sort()
        return l[-2] if len(l)>1 else -1