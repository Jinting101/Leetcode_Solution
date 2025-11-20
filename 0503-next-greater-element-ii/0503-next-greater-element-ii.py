class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        maxnum, maxind = -float('inf'), 0
        for i,x in enumerate(nums):
            if x >= maxnum:
                maxnum = x
                maxind = i
        st = []
        res = [-1] * n
        for i,x in enumerate(nums[maxind+1:] + nums[:maxind+1]):
            while st and x > st[-1][0]:
                y, ind = st.pop()
                res[ind] = x
            st.append((x, i))
        return res[n-maxind-1:] + res[:n-maxind-1]






        


        # [2, 3, 4, -1, -1]

        # 1 4 6 5 3 6 2 1 3

        # 2 1 3 1 4 6 5 3 6