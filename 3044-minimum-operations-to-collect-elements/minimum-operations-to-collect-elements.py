class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        seen = set()
        operations = 0
        for num in reversed(nums):
            operations += 1
            if num <= k:
                seen.add(num)
            if len(seen) == k:
                break
        return operations