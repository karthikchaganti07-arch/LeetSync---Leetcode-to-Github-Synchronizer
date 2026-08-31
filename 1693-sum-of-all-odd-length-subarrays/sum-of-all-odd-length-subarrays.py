from itertools import combinations
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        c=0
        for i in range(1, n+1, 2):
            for j in range(n-i+1):
                s=arr[j:j+i]
                c+=sum(s)
        return c