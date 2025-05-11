class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd, cnt = False, 0
        for x in arr:
            if x % 2 == 1:
                if not odd:
                    odd = True
                    cnt = 1
                else:
                    cnt += 1
            else:
                odd = False
                cnt = 0
            if cnt == 3:
                return True
        return False