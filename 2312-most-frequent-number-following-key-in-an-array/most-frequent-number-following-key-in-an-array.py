from collections import Counter
class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        c= Counter()
        for i in range(len(nums) - 1):
            if nums[i] == key:
                c[nums[i + 1]] += 1
        return max(c, key=lambda x: (c[x], x))