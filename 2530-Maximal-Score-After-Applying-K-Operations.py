import heapq
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        new_nums = [-x for x in nums]
        heapq.heapify(new_nums)
        while k > 0:
            num = abs(heapq.heappop(new_nums))
            score += num
            heapq.heappush(new_nums, -((num+2)//3))
            k -= 1
        return score
        