class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mapping = {key:value for key,value in knowledge}
        in_bracket=False
        l=[]
        res=[]
        for i in s:
            if i=="(":
                in_bracket=True
            elif i==")":
                in_bracket=False
                string="".join(l)
                res.append(mapping.get(string,"?"))
                l=[]
            elif in_bracket:
                l.append(i)
            else:
                res.append(i)
        return "".join(res)