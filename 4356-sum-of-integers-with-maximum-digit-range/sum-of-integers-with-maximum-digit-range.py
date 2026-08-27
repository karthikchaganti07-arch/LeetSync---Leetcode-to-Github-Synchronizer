class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        l=[]
        for i in nums:
            s=str(i)
            m=max(int(digit) for digit in s)
            mi=min(int(digit) for digit in s)
            sum=m-mi
            l.append(sum)
        m=max(l)
        c=0
        for i in range(len(l)):
            if l[i]==m:
                print(nums[i])
                c+=nums[i]
        return c