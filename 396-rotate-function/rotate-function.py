class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        n = len(nums)
        t = sum(nums)
        curr = sum(i * num for i, num in enumerate(nums))
        m = curr
        for i in range(1, n):
            curr = curr + t- n * nums[n - i]
            m = max(m, curr)
        return m