class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        m = c = 0
        d = {}
        idx = 0
        while idx < len(s):
            i = s[idx]
            if i not in d:
                d[i] = []
            if len(d[i]) == 2:
                m = max(m, c)
                idx = d[i][0] + 1
                d = {}
                c = 0
                continue  
            d[i].append(idx)
            c += 1
            idx += 1
        return max(m, c)