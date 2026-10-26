class Solution:
    def secondsBetweenTimes(self, st: str, et: str) -> int:
        sh,sm,ss=int(st[:2]),int(st[3:5]),int(st[6:])
        eh,em,es=int(et[:2]),int(et[3:5]),int(et[6:])
        if em<sm:
            eh-=1
            em+=60
        if es<ss:
            em-=1
            es+=60
        return ((eh-sh)*3600)+((em-sm)*60)+(es-ss)