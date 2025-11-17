class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        cur = 0
        prev = False
        for x in nums:
            if x == 1:
                if not prev:
                    prev = True
                    continue
                else:
                    if cur < k:
                        return False
                    else:
                        cur = 0
            else:
                if prev:
                    cur += 1
        return True