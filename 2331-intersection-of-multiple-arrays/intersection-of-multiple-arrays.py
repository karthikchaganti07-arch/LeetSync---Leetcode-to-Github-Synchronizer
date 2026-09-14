class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        r=[0]*1001
        n=len(nums)
        for arr in nums:
            for num in arr:
                r[num]+=1
        return [i for i in range(1001) if r[i] == n]