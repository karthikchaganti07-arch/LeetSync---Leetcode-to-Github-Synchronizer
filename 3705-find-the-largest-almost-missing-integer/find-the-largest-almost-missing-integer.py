from collections import Counter
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return max(nums)
        c = Counter(nums)
        valid = [x for x in (nums if k == 1 else (nums[0], nums[-1])) if c[x] == 1]
        return max(valid) if valid else -1