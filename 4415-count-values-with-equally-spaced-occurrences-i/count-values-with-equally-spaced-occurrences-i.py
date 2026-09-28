class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        return sum(
            1
            for num in set(nums)
            if (indices := [j for j, x in enumerate(nums) if x == num]) 
            and len(indices) == 3 
            and (indices[1] - indices[0] == indices[2] - indices[1])
        )