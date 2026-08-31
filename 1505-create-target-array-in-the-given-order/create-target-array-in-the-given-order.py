class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        l=[]
        for i,j in zip(nums,index):
            l.insert(j,i)
        return l