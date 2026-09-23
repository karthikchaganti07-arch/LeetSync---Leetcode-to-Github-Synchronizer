class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        for i in words:
            is_valid = all(char in allowed for char in i)
            if is_valid:
                count+=1
        return count