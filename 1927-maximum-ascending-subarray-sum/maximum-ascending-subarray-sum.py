class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        m=nums[0]
        ma=0
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                m+=nums[i]
            else:
                ma=max(m,ma)
                m=nums[i]
        return max(m,ma)