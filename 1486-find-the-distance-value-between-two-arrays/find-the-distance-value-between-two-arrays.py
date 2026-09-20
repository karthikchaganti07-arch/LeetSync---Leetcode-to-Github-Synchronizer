class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count=0
        for i in arr1:
            r=0
            for j in arr2:
                if abs(i-j)>d:
                    r+=1
            if r==len(arr2):
                count+=1
        return count