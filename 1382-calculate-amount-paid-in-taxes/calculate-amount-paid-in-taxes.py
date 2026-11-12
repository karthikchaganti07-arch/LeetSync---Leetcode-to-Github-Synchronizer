class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:
        c=0
        r=0
        for i,j in brackets:
            if income<= r:
                break
            tax= min(income,i) -r
            c+= tax*j
            r=i
        return c/ 100.0