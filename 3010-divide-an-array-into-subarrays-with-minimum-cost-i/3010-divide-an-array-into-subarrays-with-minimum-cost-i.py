class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return sum(nums)
        temp = nums[0]
        heapq.heapify(nums)
        res = temp
        i = 0
        while i < 2:
            cur = heapq.heappop(nums)
            if cur == temp:
                temp = -1
                continue
            res += cur
            i += 1
        return res

