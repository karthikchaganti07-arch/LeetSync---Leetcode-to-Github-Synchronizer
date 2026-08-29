from math import gcd

class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        n = len(nums)
        m= 0
        for i in range(n):
            for j in range(i + 1, n):
                g = gcd(nums[i], nums[j])
                curr = (nums[i] * nums[j]) // (g * g)
                if curr > m:
                    m = curr 
        return m