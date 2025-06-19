class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        prev = nums[0]
        res = 1
        for x in nums[1:]:
            if x - prev > k:
                res += 1
                prev = x
        return res