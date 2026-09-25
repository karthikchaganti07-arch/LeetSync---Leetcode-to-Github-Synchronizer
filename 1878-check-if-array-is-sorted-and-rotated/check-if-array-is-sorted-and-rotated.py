class Solution:
    def check(self, nums: list[int]) -> bool:
        n=sorted(nums)
        for i in range(len(nums)):
            if nums[i+1:]+nums[:i+1]==n:
                return True
        return False