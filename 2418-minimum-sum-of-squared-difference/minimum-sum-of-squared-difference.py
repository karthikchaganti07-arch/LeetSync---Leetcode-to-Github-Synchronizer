class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diffs = [abs(n1 - n2) for n1, n2 in zip(nums1, nums2)]
        if sum(diffs) <= k:
            return 0
        m = max(diffs)
        freq = [0] * (m + 1)
        for d in diffs:
            freq[d] += 1
        for d in range(m, 0, -1):
            if freq[d] > 0:
                take = min(k, freq[d])
                freq[d] -= take
                freq[d - 1] += take
                k -= take
                if k == 0:
                    s = 0
        for d, count in enumerate(freq):
            s += count * (d * d)
        return s