class Solution:
    def countValidPrefixes(self, s: str) -> int:
        count=0
        balance=0
        for i in s:
            if i=="1":
                balance+=1
            else:
                balance-=1
            if abs(balance)<=1:
                count+=1
        return count