class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s=str(n)
        m=0
        for i in range(len(s)):
            if i%2==0:
                m+=int(s[i])
            else:
                m-=int(s[i])
        return m