class Solution:
    def finalString(self, s: str) -> str:
        r = ""
        for char in s:
            if char != "i":
                r += char
            else:
                r = r[::-1]
        return r