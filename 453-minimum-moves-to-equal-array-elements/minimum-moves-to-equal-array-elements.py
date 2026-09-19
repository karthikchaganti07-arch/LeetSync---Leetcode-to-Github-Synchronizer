class Solution:
    def minMoves(self, nums: list[int]) -> int:
        val=min(nums)
        moves=0
        for num in nums:
            moves+=num-val
        return moves