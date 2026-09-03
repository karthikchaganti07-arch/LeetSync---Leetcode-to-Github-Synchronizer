class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mn = nums1[0]
        can_odd = False
        for i in nums1:
            if i < mn:
                mn = i
            if i & 1:
                can_odd = True
        if mn & 1:
            return True
        return not can_odd