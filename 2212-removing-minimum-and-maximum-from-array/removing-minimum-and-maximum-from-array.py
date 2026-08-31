class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        mi= nums.index(min(nums))
        ma= nums.index(max(nums))
        if mi> ma:
            mi, ma= ma, mi
        front = max(mi, ma) + 1
        back = n - min(mi, ma)
        both = (mi + 1) + (n - ma)
        return min(front, back, both)