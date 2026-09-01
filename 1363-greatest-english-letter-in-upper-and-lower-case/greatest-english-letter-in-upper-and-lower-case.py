class Solution:
    def greatestLetter(self, s: str) -> str:
        l=set(s)
        for i in reversed("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            if i in l and i.lower() in l:
                return i
        return ""