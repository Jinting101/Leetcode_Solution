class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        n = len(nums)
        if n == 1:
            return nums[0]
        def check(nums):
            l = len(nums)
            if l == 0:
                return 0
            if l == 1:
                return nums[0]
            ind = []
            cur = 1
            for i in range(l):
                cur *= nums[i]
                if nums[i] < 0:
                    ind.append(i)
            temp1 = temp2 = cur
            if len(ind) % 2 == 1:
                for i in range(ind[0]+1):
                    temp1 /= nums[i]
                for i in range(ind[-1], l):
                    temp2 /= nums[i]
            return max(cur, temp1, temp2)
        zeros = []
        for i,x in enumerate(nums):
            if x == 0:
                zeros.append(i)
        prev = 0
        for x in zeros:
            res = max(res, check(nums[prev:x]))
            prev = x+1
        return int(max(res, check(nums[prev:])))
