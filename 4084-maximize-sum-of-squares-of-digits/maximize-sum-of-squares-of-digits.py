class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > num * 9:
            return ""
        nine = sum // 9
        r = sum % 9
        zero = num - nine - (1 if r > 0 else 0)
        ans = ("9" * nine)
        if r > 0:
            ans += str(r)
        ans += ("0" * zero)
        return ans