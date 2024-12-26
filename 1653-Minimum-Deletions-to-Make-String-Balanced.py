class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = countB = 0
        for c in s:
            if c == 'b':
                countB += 1
            else:
                # // is 'a'
                # // if countB is zero, 
                # //     then res will be 0, because we do not need to remove anything
                # // in the case where countB is no longer 0
                # //     then we just need to remove the min(countB, res + 1) 
                # //     [this +1 represents the 'a' we encounter in this iteration + ans (those to be removed in previous iteration)]
                res = min(res + 1, countB)
        return res
