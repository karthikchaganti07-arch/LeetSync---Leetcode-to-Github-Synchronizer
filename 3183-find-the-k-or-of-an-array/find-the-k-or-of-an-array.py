class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        r= 0
        for i in range(31):
            p = 2 ** i
            c= 0
            for i in nums:
                if (i //p) % 2 == 1:
                    c += 1
            if c>= k:
                r+=p
        return r