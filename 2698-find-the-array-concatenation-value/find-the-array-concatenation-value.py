class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        c = 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            if left < right:
                r = str(nums[left]) + str(nums[right])
                c += int(r)
            else:
                c += nums[left]
            left += 1
            right -= 1
        return c