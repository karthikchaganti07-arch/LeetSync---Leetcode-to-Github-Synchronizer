class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        b=bin(n)[2:][::-1]
        even=odd=0
        for i,bi in enumerate(b):
            if bi=="1":
                if i%2==0:
                    even+=1
                else:
                    odd+=1
        return [even,odd]