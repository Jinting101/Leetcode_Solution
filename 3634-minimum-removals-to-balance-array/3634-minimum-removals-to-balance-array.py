class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:

        def check(nums, l, r):
            heapq.heapify(nums)
            res = 0
            heapq.heapify(nums)
            while nums and abs(r) > abs(l) * k:
                if nums[0] > 0:
                    l = heapq.heappop(nums)
                else:
                    r = heapq.heappop(nums)
                if abs(r) <= abs(l) * k:
                    return res
                res += 1
            return res
        
        l, r = min(nums), max(nums)

        return min(check(nums.copy(), l, r), check([-x for x in nums.copy()], l, r))

        

        # 100 99 98 97 1

        # 100 4 3 2 1 k=10