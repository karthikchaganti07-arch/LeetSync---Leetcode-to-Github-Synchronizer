class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        n=sorted(nums)
        c=0
        m=n[-1]
        while k>0:
            c+=m
            m+=1
            k-=1
        return c