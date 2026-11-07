from collections import Counter
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        res= Counter(s)
        r = Counter(target)
        c = float('inf')
        for i in r:
            c = min(c, res[i] // r[i])
        return c