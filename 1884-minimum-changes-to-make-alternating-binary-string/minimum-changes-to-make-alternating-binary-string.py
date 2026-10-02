class Solution:
    def minOperations(self, s: str) -> int:
        count=0
        for i in range(0,len(s)):
            expected = "0" if i % 2 == 0 else "1"
            if s[i] != expected:
                count += 1
        return min(count,len(s)-count)