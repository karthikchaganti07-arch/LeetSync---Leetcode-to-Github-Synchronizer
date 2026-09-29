class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        c = m = l = 0
        for i in range(len(s)):
            if s[i] == '1':
                if c:
                    c -= 1
                    l += 2
                else:
                    m = max(m, l)
                    c = 0
                    l = 0
            else:
                if i > 0 and s[i-1] == '1':
                    m = max(m, l)
                    c = 0
                    l = 0
                c += 1
        return max(m, l)