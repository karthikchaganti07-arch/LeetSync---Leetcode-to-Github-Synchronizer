class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
        if count == 0:
            return 0
        if count > 1:
            return -1
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                return n - i - 1