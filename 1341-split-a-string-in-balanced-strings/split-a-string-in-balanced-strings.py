class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count=0
        m=0
        for i in s:
            if i=="R":
                m+=1
            elif i=="L":
                m-=1
            if m==0:
                count+=1
        return count
            