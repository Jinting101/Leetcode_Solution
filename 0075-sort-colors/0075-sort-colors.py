class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num1, num2, num3 = 0, 0, 0
        for x in nums:
            if x == 0:
                num1 += 1
            elif x == 1:
                num2 += 1
            else:
                num3 += 1
        for i in range(len(nums)):
            if i < num1:
                nums[i] = 0
            elif i < num1+num2:
                nums[i] = 1
            else:
                nums[i] = 2