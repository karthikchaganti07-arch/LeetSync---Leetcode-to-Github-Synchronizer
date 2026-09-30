class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = max_diff = max_num = 0
        for n in nums:
            ans = max(ans, max_diff * n)
            max_diff = max(max_diff, max_num - n)
            max_num = max(max_num, n)
        return ans