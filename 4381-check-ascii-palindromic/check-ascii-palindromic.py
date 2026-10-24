class Solution:
    def isPalindromic(self, s: str) -> bool:
        r=""
        for i in s:
            m=bin(ord(i))[2:].zfill(8)
            r+=m
        print(r)
        return r==r[::-1]