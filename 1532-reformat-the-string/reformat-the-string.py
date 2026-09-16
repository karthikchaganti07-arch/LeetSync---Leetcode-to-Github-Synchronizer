class Solution:
    def reformat(self, s: str) -> str:
        if len(s)<2:
            return s
        num=[]
        alpha=[]
        for i in s:
            if i.isdigit():
                num.append(i)
            else:
                alpha.append(i)
        if not num or not alpha:
            return ""
        n=len(num)
        a=len(alpha)
        if abs(n - a) > 1:
            return ""
        res = []
        if n >= a:
            for i in range(a):
                res.append(num[i])
                res.append(alpha[i])
            if n > a:
                res.append(num[-1])
        else:
            for i in range(n):
                res.append(alpha[i])
                res.append(num[i])
            res.append(alpha[-1])
        return "".join(res)