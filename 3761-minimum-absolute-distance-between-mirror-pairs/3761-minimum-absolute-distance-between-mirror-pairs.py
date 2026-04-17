class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def rev(num):
            cur = 0
            while num:
                cur = cur * 10 + num % 10
                num //= 10
            return cur
        
        dic = {}
        res = float('inf')
        nums = nums[::-1]
        for i, num in enumerate(nums):
            rev_num = rev(num)
            if rev_num in dic:
                res = min(res, i - dic[rev_num])
            dic[num] = i

        return res if res != float('inf') else -1