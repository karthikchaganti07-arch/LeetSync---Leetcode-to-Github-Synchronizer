class Solution:
    def minInsertions(self, s: str) -> int:
        count = 0
        l = []
        i = 0
        while i < len(s):
            if s[i] == "(":
                l.append(s[i])
                i += 1
            else:
                if i + 1 < len(s) and s[i+1] == ")":
                    i += 2
                else:
                    count += 1
                    i += 1
                if l:
                    l.pop()
                else:
                    count += 1
        count += len(l)*2
        return count