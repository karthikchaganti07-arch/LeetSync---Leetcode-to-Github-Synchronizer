from collections import Counter
class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        n=len(words)
        c=Counter("".join(words))
        for i in c.values():
            if i%n!=0:
                return False
        return True