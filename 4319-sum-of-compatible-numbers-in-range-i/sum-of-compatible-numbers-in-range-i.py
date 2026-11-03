class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        start = max(1, n-k)
        end=n+k
        c=0
        for i in range(start,end+1):
            if (n & i) == 0:
                c+=i
        return c