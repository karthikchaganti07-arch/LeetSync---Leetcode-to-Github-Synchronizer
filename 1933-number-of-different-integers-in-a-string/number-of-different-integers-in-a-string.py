class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        unique = set()
        num = []
        for char in word:
            if char.isdigit():
                num.append(char)
            else:
                if num:
                    unique.add(int("".join(num)))
                    num = []
        if num:
            unique.add(int("".join(num)))
        return len(unique)