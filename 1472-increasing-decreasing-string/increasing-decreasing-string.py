from collections import Counter
class Solution:
    def sortString(self, s: str) -> str:
        count=Counter(s)
        unique_chars=sorted(count.keys())
        result=[]
        while len(result)<len(s):
            for i in unique_chars:
                if count[i]>0:
                    result.append(i)
                    count[i]-=1
            for i in reversed(unique_chars):
                if count[i]>0:
                    result.append(i)
                    count[i]-=1
        return "".join(result)