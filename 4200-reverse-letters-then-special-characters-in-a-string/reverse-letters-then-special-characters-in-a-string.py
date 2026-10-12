class Solution:
    def reverseByType(self, s: str) -> str:
        letters = [c for c in s if c.islower()]
        specials = [c for c in s if not c.islower()]
        res = []
        for c in s:
            if c.islower():
                res.append(letters.pop())
            else:
                res.append(specials.pop())        
        return "".join(res)