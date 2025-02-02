class Solution:
    def check(self, nums: List[int]) -> bool:
        res = sorted(nums)
        if nums == res:
            return True
        ind = 0
        prev = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > prev:
                ind = i
                break
            prev = nums[i]
        ind += 1
        return nums[ind:]+nums[:ind] == res

        # works for nums < 10
        # res = sorted(nums)*2
        # return ''.join(map(str, nums)) in ''.join(map(str, res))