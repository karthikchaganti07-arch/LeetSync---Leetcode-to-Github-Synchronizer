class Solution:
    def isBalanced(self, num: str) -> bool:
        l=0
        r=0
        for i in range(len(num)):
            if i%2==0:
                l+=(int(num[i]))
            else:
                r+=(int(num[i]))
        return l==r