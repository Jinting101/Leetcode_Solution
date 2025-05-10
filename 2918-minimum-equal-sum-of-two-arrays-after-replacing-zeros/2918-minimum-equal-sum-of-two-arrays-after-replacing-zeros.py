class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        cnt1, cnt2 = nums1.count(0), nums2.count(0)
        minsum = max(s1+cnt1, s2+cnt2)
        if (cnt1 == 0 and s1 < minsum) or (cnt2 == 0 and s2 < minsum):
            return -1
        return minsum
        


