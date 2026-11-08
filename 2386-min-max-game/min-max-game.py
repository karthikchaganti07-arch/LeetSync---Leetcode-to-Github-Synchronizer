class Solution:
    def minMaxGame(self, nums: list[int]) -> int:
        while len(nums) > 1:
            n= []
            for i in range(0, len(nums), 2):
                if (i // 2) % 2 == 0:
                    n.append(min(nums[i], nums[i+1]))
                else:
                    n.append(max(nums[i], nums[i+1]))
            nums = n
        return nums[-1]