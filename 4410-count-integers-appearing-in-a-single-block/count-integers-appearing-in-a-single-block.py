from collections import Counter
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        blocks = Counter()
        for i, x in enumerate(nums):
            if i == 0 or x != nums[i - 1]:
                blocks[x] += 1
        return sum(1 for count in blocks.values() if count == 1)