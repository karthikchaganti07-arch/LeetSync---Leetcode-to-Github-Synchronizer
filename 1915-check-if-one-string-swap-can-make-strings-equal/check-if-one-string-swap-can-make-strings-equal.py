class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        return sorted(s1) == sorted(s2) and sum(a!=b for a, b in zip(s1, s2))<=2