class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD=10**9+7
        p = {}
        for ch in s:
            p[ch] = (sum(p.values()) + 1) % MOD
        return sum(p.values()) % MOD