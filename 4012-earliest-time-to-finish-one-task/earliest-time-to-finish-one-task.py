class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        m=float("inf")
        for i in tasks:
            m=min(m,sum(i))
        return m