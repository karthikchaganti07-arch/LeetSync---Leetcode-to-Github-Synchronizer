class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        e=o=0
        for i in nums:
            if i%2==0:
                e+=1
            else:
                o+=1
        l=[]
        for i in nums:
            if i%2==0:
                l.append(o)
                e-=1
            else:
                l.append(e)
                o-=1
        return l