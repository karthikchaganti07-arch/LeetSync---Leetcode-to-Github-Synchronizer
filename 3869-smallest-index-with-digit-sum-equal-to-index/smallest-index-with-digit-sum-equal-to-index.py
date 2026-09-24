class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def d(x):
            s=0
            while x>0:
                s+=x%10
                x//=10
            return s
        for i in range(len(nums)):
            if d(nums[i])==i:
                return i
        return -1