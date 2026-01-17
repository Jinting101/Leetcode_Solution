class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        dic = {}

        for x in nums:
            dic[x] = dic.get(x, 0) + 1
        
        for i in range(10**4+1, -10**4-1, -1):
            if i not in dic:
                continue
            k -= dic[i]
            if k <= 0:
                return i
        
        return None



        # -10**4, -10**4+1, ...... 10**4-1, 10**4


        # 1 2 3 4 5 6

        # 1 1 1 1 2 1
