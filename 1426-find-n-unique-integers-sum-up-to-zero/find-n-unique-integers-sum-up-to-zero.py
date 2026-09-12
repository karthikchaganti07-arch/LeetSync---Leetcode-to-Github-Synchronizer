class Solution:
    def sumZero(self, n: int) -> List[int]:
        r=[]
        if n%2==1:
            r.append(0)
        for i in range(1,n//2+1):
            r.append(i)
            r.append(-i)
        return r