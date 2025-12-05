class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        res = 0
        leftSum = 0
        rightSum = sum(nums)
        for x in nums[:-1]:
            leftSum += x
            rightSum -= x 
            if (leftSum - rightSum) % 2 == 0:
                res += 1
        return res