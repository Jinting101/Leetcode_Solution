class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num3 = nums1 + nums2
        num3.sort()
        middle = len(num3)/2
        if (middle % 1) == 0.5:
            return num3[int(middle - 0.5)]
        else:
            a = num3[int(middle)]
            b = num3[int(middle-1)]
            return (a + b)/2