from collections import Counter
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        c=Counter()
        for i in s:
            c[i]+=1
            if c[i]==2:
                return i