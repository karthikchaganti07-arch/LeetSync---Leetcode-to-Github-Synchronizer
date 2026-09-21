class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        if len(nums)==2:
            return 1
        l=set()
        while len(nums)>0:
            min_no=min(nums)
            max_no=max(nums)
            l.add((min_no+max_no)/2)
            nums.remove(min_no)
            nums.remove(max_no)
        return len(l)