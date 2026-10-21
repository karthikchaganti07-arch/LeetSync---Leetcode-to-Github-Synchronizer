class Solution:
    def scoreBalance(self, s: str) -> bool:
        for i in range(len(s)-1):
            c=m=0
            for j in range(i+1):
                c += ord(s[j]) - ord("a") + 1
            for j in range(i+1,len(s)):
                m+=ord(s[j])-ord("a")+1
            if m==c:
                return True
        return False