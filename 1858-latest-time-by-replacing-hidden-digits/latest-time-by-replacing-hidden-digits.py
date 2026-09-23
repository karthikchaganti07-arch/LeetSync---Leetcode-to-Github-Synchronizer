class Solution:
    def maximumTime(self, time: str) -> str:
        l=list(time)
        if l[0]=="?":
            if l[1]=="?" or l[1]<"4":
                l[0]="2"
            else:
                l[0]="1"
        if l[1]=="?":
            if l[0]=="2":
                l[1]="3"
            else:
                l[1]="9"
        if l[3]=="?":
            l[3]="5"
        if l[4]=="?":
            l[4]="9"
        return "".join(l)