class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        c=0
        n=str(num)
        for i in range(len(n)-k+1):
            val = int(n[i:i+k])
            if val!=0 and num%val==0:
                c+=1
        return c