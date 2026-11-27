class Solution:
    def minTimeToType(self, word: str) -> int:
        t = 0
        c= 'a'
        for ch in word:
            d=abs(ord(ch) - ord(c))
            t+=min(d, 26 - d) + 1
            c=ch
        return t