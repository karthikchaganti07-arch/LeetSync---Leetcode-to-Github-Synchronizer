class Solution:
    def generateTag(self, caption: str) -> str:
        result = caption.split()
        r = []
        for i, word in enumerate(result):
            if i == 0:
                new = word.lower()
            else:
                f = word[0].upper()
                s = word[1:].lower()
                new = f + s
            r.append(new)
        return ("#" + "".join(r))[:100]