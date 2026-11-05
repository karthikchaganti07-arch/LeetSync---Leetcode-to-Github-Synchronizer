class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            if i%2==0:
                c|=i
        return c