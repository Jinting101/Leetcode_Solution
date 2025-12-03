class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        MOD = 10 ** 9 + 7
        l, r = len(horizontalCuts), len(verticalCuts)
        mh, mv = 0, 0
        for i,x in enumerate(horizontalCuts):
            if i == 0:
                mh = max(mh, x)
            else:
                mh = max(mh, horizontalCuts[i] - horizontalCuts[i-1])

            if i == l-1:
                mh = max(mh, h-x)
                
        for i,x in enumerate(verticalCuts):
            if i == 0:
                mv = max(mv, x)
            else:
                mv = max(mv, verticalCuts[i] - verticalCuts[i-1])

            if i == r-1:
                mv = max(mv, w-x)
                
        return mh * mv % MOD
