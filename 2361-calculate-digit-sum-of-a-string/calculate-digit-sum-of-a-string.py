class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            l = []
            for i in range(0, len(s), k):
                r= s[i:i+k]
                d= sum(int(ch) for ch in r)
                l.append(str(d))
            s = "".join(l)
        return s