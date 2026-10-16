import re
class Solution:
    def reformatNumber(self, number: str) -> str:
        l=re.split(r"[ -]", number)
        number="".join(l)
        res = []
        n = len(number)
        for i in range(0, n, 3):
            if n - i == 4:
                res.append(number[i:i+2])
                res.append(number[i+2:i+4])
                break
            else:
                res.append(number[i:i+3])
        return "-".join(res)