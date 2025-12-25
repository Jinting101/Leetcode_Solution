class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res = 0
        steps, l = 0, 0
        while l < k:
            if happiness[l] - steps <= 0:
                break
            res += (happiness[l] - steps)
            steps += 1
            l += 1
        return res