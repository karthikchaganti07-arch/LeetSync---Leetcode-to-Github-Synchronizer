class Solution:
    def findIndices(self, nums: List[int], ind: int, val: int) -> List[int]:
        
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if abs(i-j)>=ind and abs(nums[i]-nums[j])>=val:
                    return [i,j]
        return [-1,-1]