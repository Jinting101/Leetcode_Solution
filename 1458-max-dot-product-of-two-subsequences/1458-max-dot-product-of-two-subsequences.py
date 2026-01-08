class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)

        cur1, cur2 = min(nums1), max(nums2)
        if cur1 > 0 and cur2 < 0:
            return cur1 * cur2
        c1, c2 = max(nums1), min(nums2)
        if c1 < 0 and c2 > 0:
            return c1 * c2

        @cache
        def dp(idx1, idx2):
            if idx1 == m or idx2 == n:
                return 0
            cur = max(nums1[idx1] * nums2[idx2] + dp(idx1+1, idx2+1),
                    dp(idx1+1, idx2),
                    dp(idx1, idx2+1))
            return cur

        return dp(0, 0)