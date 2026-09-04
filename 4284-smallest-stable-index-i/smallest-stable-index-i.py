class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        res=[]
        for i in range(len(nums)):
            l=max(nums[:i+1])
            r=min(nums[i:n])
            if l-r<=k:
                return i
        return -1