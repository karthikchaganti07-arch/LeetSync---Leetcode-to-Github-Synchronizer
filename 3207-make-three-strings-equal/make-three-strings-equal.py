class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        min_len = min(len(s1), len(s2), len(s3))
        l = 0
        while l < min_len and s1[l] == s2[l] == s3[l]:
            l += 1
        if l == 0:
            return -1
        return len(s1) + len(s2) + len(s3) - 3 * l