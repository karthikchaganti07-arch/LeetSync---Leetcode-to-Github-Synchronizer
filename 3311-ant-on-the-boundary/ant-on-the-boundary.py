class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        c=0
        b=0
        for i in nums:
            c+=i
            if c==0:
                b+=1
        return b