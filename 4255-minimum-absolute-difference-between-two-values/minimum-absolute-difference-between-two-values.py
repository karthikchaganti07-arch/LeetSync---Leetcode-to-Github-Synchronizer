class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        while nums and nums[0] == 0:
            nums.pop(0)
        if not nums:
            return -1
        l1 = -1
        l2 = -1
        m=float("inf")
        for i in range(len(nums)):
            if nums[i] == 1:
                l1 = i
                if l2 != -1:
                    m = min(m, abs(i - l2))
            elif nums[i] == 2:
                l2 = i
                if l1 != -1:
                    m = min(m, abs(i - l1))
        return m if m != float("inf") else -1