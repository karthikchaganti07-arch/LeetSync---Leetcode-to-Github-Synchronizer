class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [n] * n
        d = n
        for i in range(n):
            if s[i] == c:
                d = 0
            else:
                d += 1
            ans[i] = d
        d = n
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                d = 0
            else:
                d += 1
            ans[i] = min(ans[i], d)
        return ans