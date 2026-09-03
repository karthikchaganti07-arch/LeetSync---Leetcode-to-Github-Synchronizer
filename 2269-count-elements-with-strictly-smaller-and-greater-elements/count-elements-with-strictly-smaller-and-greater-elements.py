class Solution:
    def countElements(self, nums: List[int]) -> int:
        c=0
        mi=min(nums)
        ma=max(nums)
        for i in nums:
            if mi<i<ma:
                c+=1
        return c