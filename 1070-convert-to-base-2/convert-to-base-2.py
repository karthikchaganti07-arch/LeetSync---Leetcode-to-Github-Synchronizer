class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        ans = []
        while n != 0:
            r = n % 2
            ans.append(str(r))
            n = (n - r) // -2
        return ''.join(reversed(ans))