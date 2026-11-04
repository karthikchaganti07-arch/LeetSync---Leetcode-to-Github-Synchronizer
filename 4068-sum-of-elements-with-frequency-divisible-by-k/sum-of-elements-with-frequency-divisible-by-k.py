from collections import Counter
class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        c=Counter(nums)
        s=0
        for i in c:
            if c[i]%k==0:
                s+=i*c[i]
        return s