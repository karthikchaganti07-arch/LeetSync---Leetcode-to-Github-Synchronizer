class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        seen = {}
        for i, char in enumerate(s):
            if char in seen:
                actual = i - seen[char] - 1
                expected = distance[ord(char) - ord('a')]
                if actual != expected:
                    return False
            else:
                seen[char] = i      
        return True