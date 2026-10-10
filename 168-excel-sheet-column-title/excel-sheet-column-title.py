class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s=""
        while columnNumber>0:
            columnNumber -= 1
            rem = columnNumber % 26
            s+=(chr(ord('A') + rem))
            columnNumber //= 26
        return s[::-1]