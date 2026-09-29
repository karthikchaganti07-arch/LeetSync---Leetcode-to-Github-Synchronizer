class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            s = str(num)
            m = max(s)
            ans += int(m* len(s))
        return ans