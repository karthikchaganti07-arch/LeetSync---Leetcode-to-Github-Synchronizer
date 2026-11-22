class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        r=len(s)%k
        groups=[]
        if r:
            groups.append(s[:r])
        for i in range(r, len(s), k):
            groups.append(s[i:i + k])
        return "-".join(groups)