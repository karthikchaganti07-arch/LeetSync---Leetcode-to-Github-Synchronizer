class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        r = ""
        c = 1
        for i in num:
            if c != 0:
                if int(i) < change[int(i)]:
                    r += str(change[int(i)])
                    c -= 1
                else:
                    r += i
            else:
                if int(i) <= change[int(i)]:
                    r += str(change[int(i)])
                else:
                    r += i
                    break
        return r + num[len(r):]