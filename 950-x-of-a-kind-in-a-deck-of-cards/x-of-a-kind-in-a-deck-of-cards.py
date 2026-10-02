from collections import Counter
from math import gcd
class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        c=Counter(deck)
        g=0
        for i in c:
            g=gcd(g,c[i])
        return g>=2