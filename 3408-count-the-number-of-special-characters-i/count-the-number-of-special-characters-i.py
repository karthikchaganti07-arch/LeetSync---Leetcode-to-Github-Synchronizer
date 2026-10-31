class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c=0
        r=""
        for i in word:
            if i==i.upper():
                if i.lower() in word and i not in r:
                    c+=1
                    r+=i
        return c