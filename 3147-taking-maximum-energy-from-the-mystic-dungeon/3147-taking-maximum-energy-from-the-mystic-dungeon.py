class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        res = [-float('inf')] * n
        ene = energy[::-1]
        for i,x in enumerate(ene):
            res[i] = ene[i]
            if i - k >= 0:
                res[i] += res[i-k]
        return max(res)
 