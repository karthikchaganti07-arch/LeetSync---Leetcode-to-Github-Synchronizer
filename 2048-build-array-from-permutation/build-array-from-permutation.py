class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        r=[]
        for i in range(len(nums)):
            r.append(nums[nums[i]])
        return r