class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        l=[]
        j = 0
        for i in range(len(nums1)):
            while j < len(nums2) and nums2[j][0] < nums1[i][0]:
                l.append(nums2[j])
                j += 1
            if j < len(nums2) and nums1[i][0] == nums2[j][0]:
                l.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                j += 1
            else:
                l.append(nums1[i])
        while j < len(nums2):
            l.append(nums2[j])
            j += 1
        return l