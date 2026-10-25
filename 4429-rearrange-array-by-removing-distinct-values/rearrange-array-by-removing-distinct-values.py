from collections import Counter
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        c=Counter(nums)
        l=[]
        while c:
            s=sorted(c.keys())
            for i in s:
                l.append(i)
                c[i]-=1
                if c[i]==0:
                    del c[i]
        return l