class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        m=min(nums)
        ma=max(nums)
        diff=ma-m-(2*k)
        return max(0,diff)