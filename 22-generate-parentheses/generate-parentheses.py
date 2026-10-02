class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l=[]
        s=[("",0,0)]
        while s:
            a,b,c=s.pop()
            if b==n and c==n:
                l.append(a)
            if b<n:
                s.append((a+"(",b+1,c))
            if c<b:
                s.append((a+")",b,c+1))
        return l