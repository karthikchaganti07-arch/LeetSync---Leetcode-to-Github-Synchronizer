class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n=len(colors)
        ans=0
        for i, c in enumerate(colors):
            if c!=colors[0]:
                ans = max(ans,i)
            if c!=colors[-1]:
                ans = max(ans,n-1-i)
        return ans