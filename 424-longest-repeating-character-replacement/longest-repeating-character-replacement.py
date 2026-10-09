from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c = Counter()
        m = l = max_f = 0
        for r in range(len(s)):
            c[s[r]] += 1
            max_f = max(max_f, c[s[r]])
            if (r - l + 1) - max_f > k:
                c[s[l]] -= 1
                l += 1
            m = max(m, r - l + 1)
        return m