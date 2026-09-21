class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        f= {}
        ans = -1
        for i, ch in enumerate(s):
            if ch in f:
                ans = max(ans, i - f[ch] - 1)
            else:
                f[ch] = i
        return ans