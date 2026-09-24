class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        m=-1
        max_number=float("-inf")
        for i in divisors:
            c=0
            for j in nums:
                if j%i==0:
                    c+=1
            if m<c:
                m=c
                max_number=i
            elif m==c:
                max_number = min(max_number,i) 
        return max_number