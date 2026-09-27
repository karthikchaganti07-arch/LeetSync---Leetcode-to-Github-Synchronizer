class Solution:
    def reverseParentheses(self, s: str) -> str:
        l=[]
        res=[]
        for i in s:
            if i=="(":
                l.append(len(res))
            elif i==")":
                j=l.pop()
                res[j:]=res[j:][::-1]
            else:
                res.append(i)
        return "".join(res)