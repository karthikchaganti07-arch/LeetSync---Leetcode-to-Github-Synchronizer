class Solution:
    def countKeyChanges(self, s: str) -> int:
        d={}
        prev = s[0].lower()
        for i in s:
            char= i.lower()
            if char!= prev:
                d[char] = d.get(char, 0) + 1
            prev = char
        return sum(d.values())