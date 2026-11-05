from collections import Counter
class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        freq=Counter(nums)
        vals = sorted(freq.keys())
        for i in range(len(vals)):
            x =vals[i]
            for j in range(i + 1, len(vals)):
                y =vals[j]
                if freq[x] != freq[y]:
                    return [x, y]
        return [-1, -1]