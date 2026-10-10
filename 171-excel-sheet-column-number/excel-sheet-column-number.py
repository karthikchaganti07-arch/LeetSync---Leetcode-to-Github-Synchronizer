class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for char in columnTitle:
            val = ord(char) - ord('A') + 1
            ans = ans * 26 + val
        return ans