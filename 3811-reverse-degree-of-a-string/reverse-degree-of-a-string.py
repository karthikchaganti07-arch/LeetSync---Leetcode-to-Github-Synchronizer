class Solution(object):
    def reverseDegree(self, s):
        t=0
        l = list(s.lower())
        for i in range(len(l)): 
            r = 26 - (ord(l[i]) - ord('a'))
            t+= r*(i+1)
        return t