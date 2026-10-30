class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        l=text.split()
        c=0
        for i in l:
            r=""
            for j in i:
                if j not in brokenLetters:
                    r+=j
            if r==i:
                c+=1
        return c